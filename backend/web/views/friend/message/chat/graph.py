import os
from typing import TypedDict, Annotated, Sequence

import lancedb
from django.utils.timezone import localtime, now
from langchain_community.vectorstores import LanceDB
from langchain_core.messages import BaseMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.constants import START, END
from langgraph.graph import add_messages, StateGraph
from langgraph.prebuilt import ToolNode

from web.documents.utils.custom_embeddings import CustomEmbeddings
'''
 这个Graph类只是为了方便封装 STATE -AGENT -CONDITION(判断是否调用工具) -Tool
                                                                -END                                  
'''
class ChatGraph:
    @staticmethod
    def create_app():
        #工具节点
        @tool
        def get_time() -> str:
            """当需要查询精确时间时，调用此函数。返回格式为：[年-月-日 时:分:秒]"""
            return localtime(now()).strftime('%Y-%m-%d %H:%M:%S')

        # 知识库工具节点
        @tool
        def search_knowledge_base(query: str) -> str:
            """当用户查询阿里云百炼平台的相关信息时，调用此函数。输入为要查询的问题，输出为查询结果。"""
            db = lancedb.connect('./web/documents/lancedb_storage')
            embeddings = CustomEmbeddings()
            vector_db = LanceDB(
                connection=db,
                embedding=embeddings,
                table_name='my_knowledge_base',
            )
            docs = vector_db.similarity_search(query, k=3)
            context = '\n\n'.join([f'内容片段：{i + 1}\n{doc.page_content}' for i, doc in enumerate(docs)])
            return f'从知识库中找到以下相关信息：\n\n{context}\n'

        tools = [get_time, search_knowledge_base]
        '连接大模型 treaming=True为设置流式输出'
        llm = ChatOpenAI(
            model='deepseek-v3.2',
            openai_api_key=os.getenv('API_KEY'),
            openai_api_base=os.getenv('API_BASE'),
            streaming=True,
            model_kwargs={
                "stream_options": {
                    "include_usage": True,  # 输出token消耗数量
                }
            }
        ).bind_tools(tools)
        #'定义Agent状态 也是Langgraph数据类型 输入的内容和agent生成内容拼接后输入'
        class AgentState(TypedDict):
            messages: Annotated[Sequence[BaseMessage], add_messages]
        #'Agent逻辑'
        def model_call(state: AgentState) -> AgentState:
            res = llm.invoke(state['messages'])
            return {'messages': [res]}
        #路由节点 判断是否调用工具
        def should_continue(state: AgentState) -> str:
            last_message = state['messages'][-1]
            if last_message.tool_calls:
                return "tools"
            return "end"
        #定义工具节点
        tool_node = ToolNode(tools)
        #'定义状态图'
        graph = StateGraph(AgentState)
        #'添加节点'
        graph.add_node('agent', model_call)
        graph.add_node('tools', tool_node)
        #'添加边 开始节点'
        graph.add_edge(START, 'agent')
        #添加条件边
        graph.add_conditional_edges(
            'agent',
            #路由到对应的节点
            should_continue,
            {
                'tools': 'tools',
                'end': END,
            }
        )
        #添加边
        graph.add_edge('tools', 'agent')
        '返回编译器'
        return graph.compile()
