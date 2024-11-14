import uuid

from langchain_core.messages import ToolMessage
from scripts.populate_database import db
from scripts.populate_database import update_dates
from graph.graph3 import part_3_graph
from utils.utilities import _print_event

# Update with the backup file so we can restart from the original place in each section
db = update_dates(db)
thread_id = str(uuid.uuid4())

config = {
    "configurable": {
        # The passenger_id is used in our flight tools to
        # fetch the user's flight information
        "passenger_id": "3442 587242",
        # Checkpoints are accessed by thread_id
        "thread_id": thread_id,
    }
}
#
# tutorial_questions = [
#     "Hi there, what time is my flight?",
#     "Am i allowed to update my flight to something sooner? I want to leave later today.",
#     "Update my flight to sometime next week then",
#     "The next available option is great",
#     "what about lodging and transportation?",
#     "Yeah i think i'd like an affordable hotel for my week-long stay (7 days). And I'll want to rent a car.",
#     "OK could you place a reservation for your recommended hotel? It sounds nice.",
#     "yes go ahead and book anything that's moderate expense and has availability.",
#     "Now for a car, what are my options?",
#     "Awesome let's just get the cheapest option. Go ahead and book for 7 days",
#     "Cool so now what recommendations do you have on excursions?",
#     "Are they available while I'm there?",
#     "interesting - i like the museums, what options are there? ",
#     "OK great pick one and book it for my second day there.",
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

_printed = set()
# We can reuse the tutorial questions from part 1 to see how it does.
# for question in tutorial_questions:
#     events = part_3_graph.stream(
#         {"messages": ("user", question)}, config, stream_mode="values"
#     )
#     for event in events:
#         _print_event(event, _printed)
#     snapshot = part_3_graph.get_state(config)
#     while snapshot.next:
#         # We have an interrupt! The agent is trying to use a tool, and the user can approve or deny it
#         # Note: This code is all outside of your graph. Typically, you would stream the output to a UI.
#         # Then, you would have the frontend trigger a new run via an API call when the user has provided input.
#         try:
#             user_input = input(
#                 "Do you approve of the above actions? Type 'y' to continue;"
#                 " otherwise, explain your requested changed.\n\n"
#             )
#         except:
#             user_input = "y"
#         if user_input.strip() == "y":
#             # Just continue
#             result = part_3_graph.invoke(
#                 None,
#                 config,
#             )
#         else:
#             # Satisfy the tool invocation by
#             # providing instructions on the requested changes / change of mind
#             result = part_3_graph.invoke(
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
#         snapshot = part_3_graph.get_state(config)

if __name__ == "__main__":
    while True:
        question = input("input question please\n\n")
        events = part_3_graph.stream(
            {"messages": ("user", question)}, config, stream_mode="values"
        )
        for event in events:
            _print_event(event, _printed)
        snapshot = part_3_graph.get_state(config)
        while snapshot.next:
            # We have an interrupt! The agent is trying to use a tool, and the user can approve or deny it
            # Note: This code is all outside of your graph. Typically, you would stream the output to a UI.
            # Then, you would have the frontend trigger a new run via an API call when the user has provided input.
            try:
                user_input = input(
                    "Do you approve of the above actions? Type 'y' to continue;"
                    " otherwise, explain your requested changed.\n\n"
                )
            except:
                user_input = "y"
            if user_input.strip() == "y":
                # Just continue
                result = part_3_graph.invoke(
                    None,
                    config,
                )
            else:
                # Satisfy the tool invocation by
                # providing instructions on the requested changes / change of mind
                result = part_3_graph.invoke(
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
            snapshot = part_3_graph.get_state(config)
