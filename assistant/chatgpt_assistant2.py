import os
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig
from tools.car_rental_tools import search_car_rentals, book_car_rental, update_car_rental, cancel_car_rental
from tools.excursion_tools import search_trip_recommendations, book_excursion, update_excursion, cancel_excursion
from tools.flight_tools import fetch_user_flight_information, search_flights, update_ticket_to_new_flight, cancel_ticket
from tools.hotel_tools import search_hotels, book_hotel, update_hotel, cancel_hotel
from tools.lookup_policy import lookup_policy
from dotenv import load_dotenv
from state.state2 import State

load_dotenv()  # 加载 .env 文件中的环境变量

# Assistant 类，用于处理调用逻辑
class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        while True:
            result = self.runnable.invoke(state)
            # 检查是否有返回内容，若无则重新生成提示信息
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

# 使用 ChatOpenAI 替换 ChatAnthropic
llm = ChatOpenAI(model="gpt-4-turbo", temperature=1, api_key=os.getenv('OPENAI_API_KEY'))

# 创建提示模板
assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful customer support assistant for Swiss Airlines. "
            " Use the provided tools to search for flights, company policies, and other information to assist the user's queries. "
            " When searching, be persistent. Expand your query bounds if the first search returns no results. "
            " If a search comes up empty, expand your search before giving up."
            "\n\nCurrent user:\n<User>\n{user_info}\n</User>"
            "\nCurrent time: {time}.",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())

# 定义可用的工具
part_2_tools = [
    TavilySearchResults(max_results=1, tavily_api_key=os.getenv('TAVILY_API_KEY')),
    fetch_user_flight_information,
    search_flights,
    lookup_policy,
    update_ticket_to_new_flight,
    cancel_ticket,
    search_car_rentals,
    book_car_rental,
    update_car_rental,
    cancel_car_rental,
    search_hotels,
    book_hotel,
    update_hotel,
    cancel_hotel,
    search_trip_recommendations,
    book_excursion,
    update_excursion,
    cancel_excursion,
]

# 绑定工具并创建 Assistant 实例
part_2_assistant_runnable = assistant_prompt | llm.bind_tools(part_2_tools)
