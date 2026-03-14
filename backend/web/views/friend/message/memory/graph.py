import os
from typing import TypedDict, Annotated, Sequence

from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.constants import START, END
from langgraph.graph import add_messages, StateGraph


class MemoryGraph:
    @staticmethod
    def create_app():
        llm = ChatOpenAI(
            model='deepseek-v3.2',
            openai_api_key=os.getenv('API_KEY'),
            openai_api_base=os.getenv('API_BASE'),
        )
        #'定义Agent状态 也是Langgraph数据类型 输入的内容和agent生成内容拼接后输入'
        class AgentState(TypedDict):
            messages: Annotated[Sequence[BaseMessage], add_messages]
        #'Agent逻辑'
        def model_call(state: AgentState) -> AgentState:
            res = llm.invoke(state['messages'])
            return {'messages': [res]}

        graph = StateGraph(AgentState)
        graph.add_node('agent', model_call)

        graph.add_edge(START, 'agent')
        graph.add_edge('agent', END)

        return graph.compile()
