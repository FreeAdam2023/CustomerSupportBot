"""
@Time ： 2024-10-28
@Auth ： Adam Lyu
"""
from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import AnyMessage, add_messages


def update_dialog_stack(left: list[str], right: Optional[str]) -> list[str]:
    """Push or pop the state."""
    # 打印当前输入的参数
    print("当前堆栈 (left):", left)
    print("操作 (right):", right)

    # 根据操作更新堆栈
    if right is None:
        result = left
    elif right == "pop":
        result = left[:-1]
    else:
        result = left + [right]

    # 打印更新后的堆栈状态
    print("更新后的堆栈:", result)
    return result


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    user_info: str
    dialog_state: Annotated[
        list[
            Literal[
                "assistant",
                "update_flight",
                "book_car_rental",
                "book_hotel",
                "book_excursion",
            ]
        ],
        update_dialog_stack,
    ]
