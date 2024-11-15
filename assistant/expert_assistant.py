"""
@Time ： 2024-10-28
@Auth ： Adam Lyu
"""
import json
import os
from datetime import datetime

from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig
from langchain_openai import ChatOpenAI

from state.state import State
from pydantic import BaseModel, Field

from tools.car_rental_tools import search_car_rentals, book_car_rental, update_car_rental, cancel_car_rental
from tools.excursion_tools import search_trip_recommendations, book_excursion, update_excursion, cancel_excursion
from tools.flight_tools import update_ticket_to_new_flight, cancel_ticket, search_flights
from tools.hotel_tools import search_hotels, book_hotel, update_hotel, cancel_hotel
from tools.lookup_policy import lookup_policy


class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        while True:
            # print(f"state -> {state}")
            # print(json.dumps(state, indent=4, ensure_ascii=False))
            result = self.runnable.invoke(state)

            if not result.tool_calls and (
                    not result.content
                    or isinstance(result.content, list)
                    and not result.content[0].get("text")
            ):
                messages = state["messages"] + [("user", "Respond with a real output.")]
                state = {**state, "messages": messages}
            else:
                break
        return {"messages": result}


class CompleteOrEscalate(BaseModel):
    """A tool to mark the current task as completed and/or to escalate control of the dialog to the main assistant,
    who can re-route the dialog based on the user's needs."""

    cancel: bool = True
    reason: str

    class Config:
        json_schema_extra = {
            "example": {
                "cancel": True,
                "reason": "User changed their mind about the current task.",
            },
            "example 2": {
                "cancel": True,
                "reason": "I have fully completed the task.",
            },
            "example 3": {
                "cancel": False,
                "reason": "I need to search the user's emails or calendar for more information.",
            },
        }



# Flight booking assistant
#
# [
#     (
#         "system",
#         "你是一位专门处理航班更新的助手。当用户需要帮助更新预订时，主助手会将工作委派给你。"
#         "请确认更新后的航班详情，并告知客户任何额外费用。"
#         "在搜索时，请保持耐心。如果首次搜索未返回结果，请扩大查询范围。"
#         "如果需要更多信息或客户改变了主意，请将任务上报回主助手。"
#         "记住，只有在成功使用相关工具后，预订才算完成。"
#         "\n\n当前用户的航班信息：\n<航班>\n{user_info}\n</航班>"
#         "\n当前时间：{time}。"
#         "\n\n如果用户需要帮助，而你没有适当的工具可以使用，则"
#         '使用 "CompleteOrEscalate" 将对话返回给主助手。不要浪费用户的时间。不要编造无效的工具或功能。',
#     ),
#     ("placeholder", "{messages}"),
# ]

llm = ChatOpenAI(model="gpt-4-turbo", temperature=1, api_key=os.getenv('OPENAI_API_KEY')) # gpt-4-turbo  gpt-3.5-turbo

flight_booking_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a specialized assistant for handling flight updates. "
            " The primary assistant delegates work to you whenever the user needs help updating their bookings. "
            "Confirm the updated flight details with the customer and inform them of any additional fees. "
            " When searching, be persistent. Expand your query bounds if the first search returns no results. "
            "If you need more information or the customer changes their mind, escalate the task back to the main assistant."
            " Remember that a booking isn't completed until after the relevant tool has successfully been used."
            "\n\nCurrent user flight information:\n<Flights>\n{user_info}\n</Flights>"
            "\nCurrent time: {time}."
            "\n\nIf the user needs help, and none of your tools are appropriate for it, then"
            ' "CompleteOrEscalate" the dialog to the host assistant. Do not waste the user\'s time. Do not make up invalid tools or functions.',
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())

update_flight_safe_tools = [search_flights]
update_flight_sensitive_tools = [update_ticket_to_new_flight, cancel_ticket]
update_flight_tools = update_flight_safe_tools + update_flight_sensitive_tools
update_flight_runnable = flight_booking_prompt | llm.bind_tools(
    update_flight_tools + [CompleteOrEscalate]
)

# [
#     (
#         "system",
#         "你是一位专门处理酒店预订的助手。当用户需要帮助预订酒店时，主助手会将工作委派给你。"
#         "根据用户的偏好搜索可用的酒店，并与客户确认预订详情。"
#         "在搜索时，请保持耐心。如果首次搜索未返回结果，请扩大查询范围。"
#         "如果需要更多信息或客户改变了主意，请将任务上报回主助手。"
#         "记住，只有在成功使用相关工具后，预订才算完成。"
#         "\n当前时间：{time}。"
#         '\n\n如果用户需要帮助，而你没有适当的工具可以使用，则使用 "CompleteOrEscalate" 将对话返回给主助手。'
#         "不要浪费用户的时间。不要编造无效的工具或功能。"
#         "\n\n以下是一些需要使用 CompleteOrEscalate 的示例：\n"
#         " - '今年这个时候天气怎么样？'\n"
#         " - '算了，我觉得我自己预订'\n"
#         " - '我需要安排那边的交通'\n"
#         " - '哦，等等，我还没订机票，我会先订机票'\n"
#         " - '酒店预订已确认'",
#     ),
#     ("placeholder", "{messages}"),
# ]

# Hotel Booking Assistant
book_hotel_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a specialized assistant for handling hotel bookings. "
            "The primary assistant delegates work to you whenever the user needs help booking a hotel. "
            "Search for available hotels based on the user's preferences and confirm the booking details with the customer. "
            " When searching, be persistent. Expand your query bounds if the first search returns no results. "
            "If you need more information or the customer changes their mind, escalate the task back to the main assistant."
            " Remember that a booking isn't completed until after the relevant tool has successfully been used."
            "\nCurrent time: {time}."
            '\n\nIf the user needs help, and none of your tools are appropriate for it, then "CompleteOrEscalate" the dialog to the host assistant.'
            " Do not waste the user's time. Do not make up invalid tools or functions."
            "\n\nSome examples for which you should CompleteOrEscalate:\n"
            " - 'what's the weather like this time of year?'\n"
            " - 'nevermind i think I'll book separately'\n"
            " - 'i need to figure out transportation while i'm there'\n"
            " - 'Oh wait i haven't booked my flight yet i'll do that first'\n"
            " - 'Hotel booking confirmed'",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())

book_hotel_safe_tools = [search_hotels]
book_hotel_sensitive_tools = [book_hotel, update_hotel, cancel_hotel]
book_hotel_tools = book_hotel_safe_tools + book_hotel_sensitive_tools
book_hotel_runnable = book_hotel_prompt | llm.bind_tools(
    book_hotel_tools + [CompleteOrEscalate]
)

# [
#     (
#         "system",
#         "你是一位专门处理租车预订的助手。当用户需要帮助预订租车时，主助手会将工作委派给你。"
#         "根据用户的偏好搜索可用的租车选项，并与客户确认预订详情。"
#         "在搜索时，请保持耐心。如果首次搜索未返回结果，请扩大查询范围。"
#         "如果需要更多信息或客户改变了主意，请将任务上报回主助手。"
#         "记住，只有在成功使用相关工具后，预订才算完成。"
#         "\n当前时间：{time}。"
#         "\n\n如果用户需要帮助，而你没有适当的工具可以使用，则"
#         '使用 "CompleteOrEscalate" 将对话返回给主助手。不要浪费用户的时间。不要编造无效的工具或功能。'
#         "\n\n以下是一些需要使用 CompleteOrEscalate 的示例：\n"
#         " - '今年这个时候天气怎么样？'\n"
#         " - '有哪些航班可供选择？'\n"
#         " - '算了，我觉得我自己预订'\n"
#         " - '哦，等等，我还没订机票，我会先订机票'\n"
#         " - '租车预订已确认'",
#     ),
#     ("placeholder", "{messages}"),
# ]


# Car Rental Assistant
book_car_rental_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a specialized assistant for handling car rental bookings. "
            "The primary assistant delegates work to you whenever the user needs help booking a car rental. "
            "Search for available car rentals based on the user's preferences and confirm the booking details with the customer. "
            " When searching, be persistent. Expand your query bounds if the first search returns no results. "
            "If you need more information or the customer changes their mind, escalate the task back to the main assistant."
            " Remember that a booking isn't completed until after the relevant tool has successfully been used."
            "\nCurrent time: {time}."
            "\n\nIf the user needs help, and none of your tools are appropriate for it, then "
            '"CompleteOrEscalate" the dialog to the host assistant. Do not waste the user\'s time. Do not make up invalid tools or functions.'
            "\n\nSome examples for which you should CompleteOrEscalate:\n"
            " - 'what's the weather like this time of year?'\n"
            " - 'What flights are available?'\n"
            " - 'nevermind i think I'll book separately'\n"
            " - 'Oh wait i haven't booked my flight yet i'll do that first'\n"
            " - 'Car rental booking confirmed'",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())

book_car_rental_safe_tools = [search_car_rentals]
book_car_rental_sensitive_tools = [
    book_car_rental,
    update_car_rental,
    cancel_car_rental,
]
book_car_rental_tools = book_car_rental_safe_tools + book_car_rental_sensitive_tools
book_car_rental_runnable = book_car_rental_prompt | llm.bind_tools(
    book_car_rental_tools + [CompleteOrEscalate]
)

# Excursion Assistant
# [
#     (
#         "system",
#         "你是一位专门处理旅行推荐的助手。当用户需要帮助预订推荐的旅行时，主助手会将工作委派给你。"
#         "根据用户的偏好搜索可用的旅行推荐，并与客户确认预订详情。"
#         "如果需要更多信息或客户改变了主意，请将任务上报回主助手。"
#         "在搜索时，请保持耐心。如果首次搜索未返回结果，请扩大查询范围。"
#         "记住，只有在成功使用相关工具后，预订才算完成。"
#         "\n当前时间：{time}。"
#         '\n\n如果用户需要帮助，而你没有适当的工具可以使用，则使用 "CompleteOrEscalate" 将对话返回给主助手。'
#         "不要浪费用户的时间。不要编造无效的工具或功能。"
#         "\n\n以下是一些需要使用 CompleteOrEscalate 的示例：\n"
#         " - '算了，我觉得我自己预订'\n"
#         " - '我需要安排那边的交通'\n"
#         " - '哦，等等，我还没订机票，我会先订机票'\n"
#         " - '行程预订已确认！'",
#     ),
#     ("placeholder", "{messages}"),
# ]

book_excursion_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a specialized assistant for handling trip recommendations. "
            "The primary assistant delegates work to you whenever the user needs help booking a recommended trip. "
            "Search for available trip recommendations based on the user's preferences and confirm the booking details with the customer. "
            "If you need more information or the customer changes their mind, escalate the task back to the main assistant."
            " When searching, be persistent. Expand your query bounds if the first search returns no results. "
            " Remember that a booking isn't completed until after the relevant tool has successfully been used."
            "\nCurrent time: {time}."
            '\n\nIf the user needs help, and none of your tools are appropriate for it, then "CompleteOrEscalate" the dialog to the host assistant. Do not waste the user\'s time. Do not make up invalid tools or functions.'
            "\n\nSome examples for which you should CompleteOrEscalate:\n"
            " - 'nevermind i think I'll book separately'\n"
            " - 'i need to figure out transportation while i'm there'\n"
            " - 'Oh wait i haven't booked my flight yet i'll do that first'\n"
            " - 'Excursion booking confirmed!'",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())

book_excursion_safe_tools = [search_trip_recommendations]
book_excursion_sensitive_tools = [book_excursion, update_excursion, cancel_excursion]
book_excursion_tools = book_excursion_safe_tools + book_excursion_sensitive_tools
book_excursion_runnable = book_excursion_prompt | llm.bind_tools(
    book_excursion_tools + [CompleteOrEscalate]
)


# Primary Assistant
class ToFlightBookingAssistant(BaseModel):
    """Transfers work to a specialized assistant to handle flight updates and cancellations."""
    # 更新飞行助理在继续之前应澄清任何必要的后续问题。
    request: str = Field(
        description="Any necessary followup questions the update flight assistant should clarify before proceeding."
    )


class ToBookCarRental(BaseModel):
    """Transfers work to a specialized assistant to handle car rental bookings."""

    location: str = Field(
        description="The location where the user wants to rent a car." # 用户想要租车的地点。
    )
    start_date: str = Field(description="The start date of the car rental.")
    end_date: str = Field(description="The end date of the car rental.")
    request: str = Field(
        description="Any additional information or requests from the user regarding the car rental."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "location": "Basel",
                "start_date": "2023-07-01",
                "end_date": "2023-07-05",
                "request": "I need a compact car with automatic transmission.",
            }
        }


class ToHotelBookingAssistant(BaseModel):
    """Transfer work to a specialized assistant to handle hotel bookings."""

    location: str = Field(
        description="The location where the user wants to book a hotel."
    )
    checkin_date: str = Field(description="The check-in date for the hotel.")
    checkout_date: str = Field(description="The check-out date for the hotel.")
    request: str = Field(
        description="Any additional information or requests from the user regarding the hotel booking."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "location": "Zurich",
                "checkin_date": "2023-08-15",
                "checkout_date": "2023-08-20",
                "request": "I prefer a hotel near the city center with a room that has a view.",
            }
        }


class ToBookExcursion(BaseModel):
    """Transfers work to a specialized assistant to handle trip recommendation and other excursion bookings."""

    location: str = Field(
        description="The location where the user wants to book a recommended trip."
    )
    request: str = Field(
        description="Any additional information or requests from the user regarding the trip recommendation."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "location": "Lucerne",
                "request": "The user is interested in outdoor activities and scenic views.",
            }
        }


# The top-level assistant performs general Q&A and delegates specialized tasks to other assistants.
# The task delegation is a simple form of semantic routing / does simple intent detection
# llm = ChatAnthropic(model="claude-3-haiku-20240307")
# llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=1)

# [
#     (
#         "system",
#         "你是瑞士航空的客户支持助手。"
#         "你的主要职责是搜索航班信息和公司政策，以解答客户的询问。"
#         "如果客户要求更新或取消航班，预订租车、酒店或旅行推荐，请通过调用相应的工具将任务委派给适当的专门助手。"
#         "你自己无法进行这些类型的更改，只有专门助手才有权限为用户执行这些操作。"
#         "用户并不知道有不同的专门助手，因此不要提及它们；只需通过功能调用安静地委派任务即可。"
#         "为客户提供详细的信息，并在得出信息不可用的结论之前务必仔细检查数据库。"
#         "在搜索时，请保持耐心。如果首次搜索未返回结果，请扩大查询范围。"
#         "如果搜索无结果，请扩展搜索范围后再放弃。"
#         "\n\n当前用户的航班信息：\n<航班>\n{user_info}\n</航班>"
#         "\n当前时间：{time}。",
#     ),
#     ("placeholder", "{messages}"),
# ]

primary_assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful customer support assistant for Swiss Airlines. "
            "Your primary role is to search for flight information and company policies to answer customer queries. "
            "If a customer requests to update or cancel a flight, book a car rental, book a hotel, or get trip recommendations, "
            "delegate the task to the appropriate specialized assistant by invoking the corresponding tool. You are not able to make these types of changes yourself."
            " Only the specialized assistants are given permission to do this for the user."
            "The user is not aware of the different specialized assistants, so do not mention them; just quietly delegate through function calls. "
            "Provide detailed information to the customer, and always double-check the database before concluding that information is unavailable. "
            " When searching, be persistent. Expand your query bounds if the first search returns no results. "
            " If a search comes up empty, expand your search before giving up."
            "\n\nCurrent user flight information:\n<Flights>\n{user_info}\n</Flights>"
            "\nCurrent time: {time}.",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())

primary_assistant_tools = [
    TavilySearchResults(max_results=1),
    search_flights,
    lookup_policy,
]
assistant_runnable = primary_assistant_prompt | llm.bind_tools(
    primary_assistant_tools
    + [
        ToFlightBookingAssistant,
        ToBookCarRental,
        ToHotelBookingAssistant,
        ToBookExcursion,
    ]
)
