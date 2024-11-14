import uuid

from langchain_core.messages import ToolMessage
from scripts.populate_database import db
from scripts.populate_database import update_dates
from graph.graph2 import part_2_graph
from utils.utilities import _print_event

#
# # 创建一个示例对话
# tutorial_questions = [
#     "Hi there, what time is my flight?",
#     "Am I allowed to update my flight to something sooner? I want to leave later today.",
#     "Update my flight to sometime next week then",
#     "The next available option is great",
#     "What about lodging and transportation?",
#     "Yeah, I'd like an affordable hotel for my week-long stay (7 days). And I'll want to rent a car.",
#     "OK, could you place a reservation for your recommended hotel? It sounds nice.",
#     "Yes, go ahead and book anything that's moderately priced and has availability.",
#     "Now for a car, what are my options?",
#     "Awesome, let's just get the cheapest option. Go ahead and book for 7 days",
#     "Cool, so now what recommendations do you have on excursions?",
#     "Are they available while I'm there?",
#     "Interesting - I like the museums, what options are there?",
#     "OK, great. Pick one and book it for my second day there.",
# ]

tutorial_questions = [
    "你好，我的航班是什么时候？",
    # 您的航班是从巴黎戴高乐机场(CDG)飞往巴塞尔机场(BSL)的LX0112航班，定于2024年11月14日10:42分（当地时间）起飞。预计到达时间是同日12:12。请提前到机场，确保有足够时间办理登机手续。
    "我可以把航班改成早点的吗？我想今天晚些时候离开。",
    "那就把我的航班改到下周的某个时间吧。",
    "下一个可选的时间很好。",
    "住宿和交通怎么办？",
    "是的，我想找一个价格适中的酒店，住一个星期（7天）。我还想租一辆车。",
    "好的，你能为我推荐的酒店预定吗？听起来不错。",
    "好的，请预订任何价格适中的有空房的酒店。",
    "关于租车，有什么选择？",
    "太好了，那就选最便宜的选项吧。预定7天。",
    "很好，你有什么推荐的游览项目吗？",
    "这些游览项目在我在那期间有开放吗？",
    "有趣，我喜欢博物馆，有什么选项？",
    "好的，挑一个，在我到达的第二天预订。",
]

# 更新数据库
db = update_dates(db)
thread_id = str(uuid.uuid4())

config = {
    "configurable": {
        "passenger_id": "3442 587242",
        "thread_id": thread_id,
    }
}

_printed = set()


# Helper function to generate ToolMessage responses
def generate_tool_responses(event, messages):
    if hasattr(event, "tool_calls") and event.tool_calls:
        for tool_call in event.tool_calls:
            # 将响应消息附加到消息队列
            messages.append(
                ToolMessage(
                    tool_call_id=tool_call["id"],
                    content="Simulated tool response."  # 模拟响应内容
                )
            )
    return messages


# # 主循环
# for question in tutorial_questions:
#     events = part_2_graph.stream(
#         {"messages": [("user", question)]}, config, stream_mode="values"
#     )
#
#     for event in events:
#         _print_event(event, _printed)
#
#     # 获取最新对话状态
#     snapshot = part_2_graph.get_state(config)
#     while snapshot.next:
#         try:
#             user_input = input(
#                 "Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changes.\n\n"
#             )
#         except Exception as e:
#             print(f"Error in input: {e}")
#             user_input = "y"
#
#         if user_input.strip().lower() == "y":
#             result = part_2_graph.invoke(
#                 None,
#                 config,
#             )
#         else:
#             result = part_2_graph.invoke(
#                 {
#                     "messages": [
#                         ToolMessage(
#                             tool_call_id=event["messages"][-1].tool_calls[0]["id"],
#                             content=f"API call denied by user. Reasoning: '{user_input}'. Continue assisting, accounting for the user's input.",
#                         )
#                     ]
#                 },
#                 config,
#             )
#
#         # 更新 messages 以确保包含最新的对话内容
#         snapshot = part_2_graph.get_state(config)

if __name__ == "__main__":
    # 主循环
    while True:
        question = input("input question please\n\n")
        events = part_2_graph.stream(
            {"messages": [("user", question)]}, config, stream_mode="values"
        )

        for event in events:
            _print_event(event, _printed)

        # 获取最新对话状态
        snapshot = part_2_graph.get_state(config)
        while snapshot.next:
            try:
                user_input = input(
                    "Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changes.\n\n"
                )
            except Exception as e:
                print(f"Error in input: {e}")
                user_input = "y"

            if user_input.strip().lower() == "y":
                result = part_2_graph.invoke(
                    None,
                    config,
                )
            else:
                result = part_2_graph.invoke(
                    {
                        "messages": [
                            ToolMessage(
                                tool_call_id=event["messages"][-1].tool_calls[0]["id"],
                                content=f"API call denied by user. Reasoning: '{user_input}'. Continue assisting, accounting for the user's input.",
                            )
                        ]
                    },
                    config,
                )

            # 更新 messages 以确保包含最新的对话内容
            snapshot = part_2_graph.get_state(config)
