"""
@Time ： 2024-10-28
@Auth ： Adam Lyu
"""
import shutil
import uuid

from langchain_core.messages import ToolMessage
from scripts.populate_database import db
from scripts.populate_database import update_dates
from scripts.simulate_conversation import tutorial_questions
from utils.graph2 import part_2_graph
from utils.utilities import _print_event

# Update with the backup file so we can restart from the original place in each section
db = update_dates(db)
thread_id = str(uuid.uuid4())

config = {
    "configurable": {
        # The passenger_id is used in our flight tools to fetch the user's flight information
        "passenger_id": "3442 587242",
        # Checkpoints are accessed by thread_id
        "thread_id": thread_id,
    }
}

_printed = set()
# 我们可以重复使用 part 1 的 tutorial_questions，看看它的表现
for question in tutorial_questions:
    # 初始化 `messages` 字段
    events = part_2_graph.stream(
        {"messages": [("user", question)]}, config, stream_mode="values"
    )
    for event in events:
        _print_event(event, _printed)

    # 获取当前的对话状态
    snapshot = part_2_graph.get_state(config)

    # 从 snapshot 中获取 messages，初始化为空列表防止 snapshot 缺少消息
    messages = snapshot.get("messages", [])

    while snapshot.next:
        try:
            user_input = input(
                "Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changes.\n\n"
            )
        except:
            user_input = "y"

        # 更新 messages 字段并进行 invoke 调用
        if user_input.strip() == "y":
            result = part_2_graph.invoke({"messages": messages + [("user", question)]}, config)
        else:
            result = part_2_graph.invoke(
                {
                    "messages": messages + [
                        ToolMessage(
                            tool_call_id=event["messages"][-1].tool_calls[0]["id"],
                            content=f"API call denied by user. Reasoning: '{user_input}'. Continue assisting, accounting for the user's input.",
                        )
                    ]
                },
                config,
            )

        # 再次获取最新状态和消息
        snapshot = part_2_graph.get_state(config)
        messages = snapshot.get("messages", [])


