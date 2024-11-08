"""
@Time ： 2024-10-28
@Auth ： Adam Lyu
"""
import shutil
import uuid
from scripts.populate_database import db
from langchain_core.messages import ToolMessage

from graph.graph import part_4_graph
from scripts.populate_database import update_dates
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

tutorial_questions = [
    "Hi there, what time is my flight?",
    "Am i allowed to update my flight to something sooner? I want to leave later today.",
    "Update my flight to sometime next week then",
    "The next available option is great",
    "what about lodging and transportation?",
    "Yeah i think i'd like an affordable hotel for my week-long stay (7 days). And I'll want to rent a car.",
    "OK could you place a reservation for your recommended hotel? It sounds nice.",
    "yes go ahead and book anything that's moderate expense and has availability.",
    "Now for a car, what are my options?",
    "Awesome let's just get the cheapest option. Go ahead and book for 7 days",
    "Cool so now what recommendations do you have on excursions?",
    "Are they available while I'm there?",
    "interesting - i like the museums, what options are there? ",
    "OK great pick one and book it for my second day there.",
]

_printed = set()
# We can reuse the tutorial questions from part 1 to see how it does.
import logging

# 初始化日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def test_conversation():
    for question in tutorial_questions:
        events = part_4_graph.stream(
            {"messages": ("user", question)}, config, stream_mode="values"
        )
        for event in events:
            _print_event(event, _printed)
            logging.debug(f"Event processed: {event}")
        snapshot = part_4_graph.get_state(config)
        while snapshot.next:
            # 如果有中断，记录当前调用的 tool_call_id 和事件
            if 'tool_calls' in event["messages"][-1]:
                for tool_call in event["messages"][-1]['tool_calls']:
                    logging.debug(f"Handling tool call: {tool_call['id']} for function {tool_call['name']}")
            # 继续对用户请求的操作
            try:
                user_input = input("Do you approve of the above actions? Type 'y' to continue;"
                                   " otherwise, explain your requested changed.\n\n")
            except:
                user_input = "y"
            if user_input.strip() == "y":
                result = part_4_graph.invoke(
                    None,
                    config,
                )
                logging.debug(f"Invoke result: {result}")
            else:
                result = part_4_graph.invoke(
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
                logging.debug(f"Invoke result after user denial: {result}")
            snapshot = part_4_graph.get_state(config)
            logging.debug(f"New snapshot state: {snapshot}")


if __name__ == "__main__":
    while True:
        question = input("input question please\n\n")
        events = part_4_graph.stream(
            {"messages": ("user", question)}, config, stream_mode="values"
        )
        for event in events:
            _print_event(event, _printed)
            logging.debug(f"Event processed: {event}")
        snapshot = part_4_graph.get_state(config)
        while snapshot.next:
            # 如果有中断，记录当前调用的 tool_call_id 和事件
            if 'tool_calls' in event["messages"][-1]:
                for tool_call in event["messages"][-1]['tool_calls']:
                    logging.debug(f"Handling tool call: {tool_call['id']} for function {tool_call['name']}")
            # 继续对用户请求的操作
            try:
                user_input = input("Do you approve of the above actions? Type 'y' to continue;"
                                   " otherwise, explain your requested changed.\n\n")
            except:
                user_input = "y"
            if user_input.strip() == "y":
                result = part_4_graph.invoke(
                    None,
                    config,
                )
                logging.debug(f"Invoke result: {result}")
            else:
                result = part_4_graph.invoke(
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
                logging.debug(f"Invoke result after user denial: {result}")
            snapshot = part_4_graph.get_state(config)
            logging.debug(f"New snapshot state: {snapshot}")
