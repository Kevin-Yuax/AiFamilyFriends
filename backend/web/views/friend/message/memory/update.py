from django.utils.timezone import now
from langchain_core.messages import SystemMessage, HumanMessage

from web.models.friend import SystemPrompt, Message
from web.views.friend.message.memory.graph import MemoryGraph

#创建 系统消息
def create_system_message():
    system_prompts = SystemPrompt.objects.filter(title='记忆').order_by('order_number')
    prompt = ''
    for sp in system_prompts:
        prompt += sp.prompt
    return SystemMessage(prompt)

#创建 用户消息
def create_human_message(friend):
    prompt = f'【原始记忆】\n{friend.memory}\n'
    prompt += f'【最近对话】\n'
    messages = list(Message.objects.filter(friend=friend).order_by('-id')[:10])
    messages.reverse()
    for m in messages:
        prompt += f'user: {m.user_message}\n'
        prompt += f'ai: {m.output}\n'
    return HumanMessage(prompt)

# 更新记忆
def update_memory(friend):
    # 创建状态图 就是agent的状态
    app = MemoryGraph.create_app()
    #定义输入
    inputs = {
        'messages': [
            create_system_message(),
            create_human_message(friend),
        ]
    }

    res = app.invoke(inputs)
    friend.memory = res['messages'][-1].content

    friend.update_time = now()
    friend.save()
