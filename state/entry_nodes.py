"""
@Time ： 2024-10-28
@Auth ： Adam Lyu
"""
from typing import Callable

from langchain_core.messages import ToolMessage

from state.state import State


def create_entry_node(assistant_name: str, new_dialog_state: str) -> Callable:
    def entry_node(state: State) -> dict:
        tool_call_id = state["messages"][-1].tool_calls[0]["id"]
        # 该助理现在是
        # {assistant_name}。反思一下上面主持人助理和用户之间的对话。”
        # f“用户的意图未得到满足。使用提供的工具来帮助用户。记住，您是
        # {assistant_name}，”
        # “只有在您成功调用适当的工具后，预订、更新和其他操作才完成。”
        # “如果用户改变主意或需要其他任务的帮助，请调用
        # CompleteOrEscalate
        # 函数让主主持人助理接管控制权。”
        # “不要提及你是谁——只是充当助理的代理人。
        return {
            "messages": [
                ToolMessage(
                    content=f"The assistant is now the {assistant_name}. Reflect on the above conversation between the host assistant and the user."
                    f" The user's intent is unsatisfied. Use the provided tools to assist the user. Remember, you are {assistant_name},"
                    " and the booking, update, other other action is not complete until after you have successfully invoked the appropriate tool."
                    " If the user changes their mind or needs help for other tasks, call the CompleteOrEscalate function to let the primary host assistant take control."
                    " Do not mention who you are - just act as the proxy for the assistant.",
                    tool_call_id=tool_call_id,
                )
            ],
            "dialog_state": new_dialog_state,
        }

    return entry_node
