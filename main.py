"""
@Time ： 2024-10-27
@Auth ： Adam Lyu
"""
# from dotenv import load_dotenv
# import os
#
# load_dotenv()  # 加载 .env 文件中的环境变量
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
# rsp = llm.invoke("Hello, world!")
# print(rsp)

state = {'messages':
    [
        HumanMessage(content='你好，我的航班是什么时候？', additional_kwargs={}, response_metadata={},
                     id='6fdaaaa1-e710-4d77-bf69-303047232b9d'),
        AIMessage(
            content='您的航班（航班号LX0112）计划于2024年11月15日14:48从巴黎戴高乐机场出发，预计16:18到达巴塞尔机场。座位号是18E，经济舱。请确保提前到达机场办理登机手续。',
            additional_kwargs={'refusal': None}, response_metadata={
                'token_usage': {'completion_tokens': 94, 'prompt_tokens': 887, 'total_tokens': 981,
                                'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                              'accepted_prediction_tokens': 0,
                                                              'rejected_prediction_tokens': 0},
                                'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
                'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_5db30363ff', 'finish_reason': 'stop',
                'logprobs': None}, id='run-4264054c-2e8a-48ac-a1ac-a6ce093a3bf2-0',
            usage_metadata={'input_tokens': 887, 'output_tokens': 94, 'total_tokens': 981,
                            'input_token_details': {'audio': 0, 'cache_read': 0},
                            'output_token_details': {'audio': 0, 'reasoning': 0}}),
        HumanMessage(content='我可以把航班改成早点的吗？我想今天晚些时候离开。', additional_kwargs={},
                     response_metadata={}, id='b0f32259-1231-45e7-8a01-01ce8ad8175a'),
        AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_hazAV15Z2195h38XzHnLSwZT',
                                                                 'function': {
                                                                     'arguments': '{"query":"changing flight to an earlier date"}',
                                                                     'name': 'lookup_policy'},
                                                                 'type': 'function'}], 'refusal': None},
                  response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 1020,
                                                     'total_tokens': 1039,
                                                     'completion_tokens_details': {'audio_tokens': 0,
                                                                                   'reasoning_tokens': 0,
                                                                                   'accepted_prediction_tokens': 0,
                                                                                   'rejected_prediction_tokens': 0},
                                                     'prompt_tokens_details': {'audio_tokens': 0,
                                                                               'cached_tokens': 0}},
                                     'model_name': 'gpt-4-turbo-2024-04-09',
                                     'system_fingerprint': 'fp_35090ec11f', 'finish_reason': 'tool_calls',
                                     'logprobs': None}, id='run-5ae18d67-7f1e-48a0-b903-fe583b9fb384-0',
                  tool_calls=[
                      {'name': 'lookup_policy', 'args': {'query': 'changing flight to an earlier date'},
                       'id': 'call_hazAV15Z2195h38XzHnLSwZT', 'type': 'tool_call'}],
                  usage_metadata={'input_tokens': 1020, 'output_tokens': 19, 'total_tokens': 1039,
                                  'input_token_details': {'audio': 0, 'cache_read': 0},
                                  'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(
        content='\n## Booking and Cancellation\n\n1. How can I change my booking?\n\t* The ticket number must start with 724 (SWISS ticket no./plate).\n\t* The ticket was not paid for by barter or voucher (there are exceptions to voucher payments; if the ticket was paid for in full by voucher, then it may be possible to rebook online under certain circumstances. If it is not possible to rebook online because of the payment method, then you will be informed accordingly during the rebooking process).\n\t* There must be an active flight booking for your ticket. It is not possible to rebook open tickets or tickets without the corresponding flight segments online at the moment.\n\t* It is currently only possible to rebook outbound (one-way) tickets or return tickets with single flight routes (point-to-point).\n2. Which tickets/bookings cannot be rebooked online currently?\n\t* Bookings containing flight segments with other airlines\n\t* Bookings containing reservations, where a ticket has not yet been issued\n\t* Bookings with several valid tickets for the same person and route\n\t* Tickets with a status other than O (open) (A)\n\t* Bookings with segments with a status other than OK (e.g. containing flight segments with the status Waitlist) (HK|RR)\n\t* Tickets that do not display the tariff calculation (IT tickets)\n\t* Bookings that contain special services (e.g. transportation of animals/transportation of medical equipment/transportation of special sporting equipment etc.)\n\t* Tickets that are part of a group booking\n\t* Tickets on which the booking class (RBD) does not correspond to the tariff code (FareBase)\n3. Am I allowed to make changes to my online redemption booking?\n\t* Redemption bookings can not yet be changed on swiss.com.\n4. What changes can I make on my ticket?\n\t* You can change the flight and the travel dates. Change of origin and destination or name changes are not possible online.\n5. After I have made changes to the itinerary online, can I make another change?\n\t* If the fare condition allows it, it is possible to make multiple changes to the itinerary.\n6. Can a name be changed after a booking is made?\n\t* The correct name(s) of the customer travelling need to be entered in a booking. The first and last name of the passenger travelling needs to be entered exactly as in the travel documents. Entering a middle name is optional and can be added in the first name field. However, there is a character limitation for this field.\n\t* Your first and middle name is stored by the system spelled together without spaces. This is not a mistake and does not affect your booking.\n\t* Any subsequent name changes, including adding names to a ticket, are not allowed.\n7. Is it possible to apply the changes only to some of the passengers in the same booking?\n\t* The changes will always be applied to all passengers travelling together. Changes to the passenger name or number of passengers is not possible online.\n8. Until what time before departure can a flight be rebooked online?\n\t* The minimum time before departure for online rebookings depends on your departure airport. If you are departing from a Swiss airport, then you can rebook online up to three hours before departure.\n9. Will any differences in airport taxes be refunded online, if the new flight choice is cheaper?\n\t* No, online refunds are currently not possible.\n10. Why isn\'t the rebooking made in the same currency as the ticket?\n\t* Any calculations associated with the rebooking will be made in the currency of the original country of departure (Point of Commencement).\n11. Will my seat reservation be taken into account in the rebooking?\n\t* Yes, your seat reservation will be included in the rebooking.\n12. Will my special meal be included in the rebooking?\n\t* Yes, your special meal will be included.\n13. Will my additional passenger details (APIS) be included in the rebooking?\n\t* Yes, your APIS details will be included.\n14. Will the travel insurance obtained from the Europäische Reiseversicherung (European Travel Insurance) through SWISS be included in the new ticket?\n\t* Yes, the travel insurance obtained through SWISS will be included in the new ticket and will remain valid.\n15. Will I be given a new booking reference after rebooking?\n\t* No, your booking reference will stay the same after rebooking.\n16. Will I be given a new ticket number after rebooking?\n\t* Yes, you will be given a new ticket number after rebooking.\n17. Can I change my booking after checking in online?\n\t* No, only tickets with the status "Open" can be changed online.\n18. I want to change a flight booking which is part of a package purchased with a Travel Agency. What do I need to consider?\n\t* The changes processed on swiss.com are limited to the flight booking only. No changes to any other service included in your package (e.g. hotel, rental car etc.) will be processed.\n19. I want to process an online change to a flight booking which was purchased with a Travel Agency. What do I need to consider?\n\t* You can change your flight booking online, but your Travel Agency will not have access to your new electronic ticket.\n\n\n\n\n\n## How to Cancel a Swiss Air Flight: 877-5O7-7341 Step-by-Step Guide\nSwiss Air is a premium airline based in Switzerland that offers a range of domestic and international flights to passengers. However, sometimes situations arise where passengers may need to cancel their flights. In such cases, it is important to understand the Swiss Air Cancellation Policy to avoid any confusion or additional charges.\n\nSwiss International Airlines Cancellation Policy\nIn this article, we will provide you with everything you need to know about the Swiss Air Cancellation Policy, including how to cancel a Swiss Air flight, the fees associated with cancelling a flight, and the refund policy.\n\nIf you have booked a flight with Swiss Airlines but need to cancel it, it\'s important to understand their cancellation policy to avoid any unnecessary fees or charges.\nSwiss Airlines offers different fare types, each with their own specific cancellation terms and conditions. The most flexible fare types such as Flex and Business Flex allow you to cancel your flight up to 24 hours before departure without any penalty. For other fare types, cancellation fees may apply.\nIf you cancel your Swiss Airlines flight outside of the 24-hour window, cancellation fees will be charged depending on your fare type and the time of cancellation. For example, if you cancel a non-flexible economy class ticket, a cancellation fee will be charged. The closer you cancel to the departure date, the higher the cancellation fee.\nIn some cases, Swiss Airlines may allow you to make changes to your flight instead of cancelling it outright. However, these changes may also come with fees or penalties depending on your fare type and the type of change requested.\nIf Swiss Airlines cancels your flight, you may be entitled to a full refund or rebooking on another flight. However, if the cancellation is due to extraordinary circumstances such as bad weather or political unrest, Swiss Airlines may not be obligated to offer any compensation.\nIn summary, Swiss Airlines\' cancellation policy varies depending on your fare type and the time of cancellation. To avoid any unnecessary fees or charges, it\'s important to familiarise yourself with the terms and conditions of your ticket and to contact Swiss Airlines as soon as possible if you need to make changes or cancel your flight.\n\nHow to Cancel a Swiss Air Flight?\nIf you need to cancel a Swiss Air flight, you can do so online, through the mobile app, or by contacting the Swiss Air Customer Service team. To cancel a flight online, you can log in to your Swiss Air account and follow the instructions provided.\n\nSwiss Air Flight Cancellations Online\nIf you need to cancel a Swiss Air flight, you can do so by following these steps:\n\nVisit the Swiss Air website or app and navigate to the "My Bookings" section.\nLog in with your booking details.\nFind the flight you want to cancel and click on the "Cancel" button.\nFollow the prompts to confirm your cancellation.\nReview the cancellation policy and any fees that may apply.\nIf eligible for a refund, submit a refund request through the website or app.\nAlternatively, you can also cancel your Swiss Air flight by contacting their customer service department via phone, email or live chat. Be sure to have your booking details ready when you contact them. Keep in mind that depending on the fare type and the timing of your cancellation, you may be subject to fees or penalties.\n\nIf you choose to cancel your flight through the Swiss Air Customer Service team, you can contact them through the phone or email. It is important to note that cancellation fees may apply depending on the type of ticket you have purchased.\n\nSwiss Air Flight Cancellations via Call\nStep 1: Find the Customer Service Number\n\nThe first step is to find the Swiss Air customer service number. You can find this number on the Swiss Air website or on your booking confirmation email.\n\nStep 2: Call the Customer Service\n\nOnce you have the number, call the Swiss Air customer service team. You will be prompted to choose your language, and then you will be connected to a representative.\n\nStep 3: Provide your Flight Details\n\nProvide your flight details, including your booking reference number, flight number, and departure date. The representative will confirm your flight details and ask you why you want to cancel your flight.\n\nStep 4: Confirm the Cancellation\n\nConfirm that you want to cancel your flight. The representative will let you know if there are any cancellation fees or penalties associated with your ticket, and what your refund options are.\n\nStep 5: Receive Confirmation\n\nYou will receive a confirmation email once your cancellation has been processed. Make sure to save this email for your records.\n\nSwiss Air Flight Cancellations at Airport\nStep 1: Go to the Airport\n\nIf you\'re cancelling your Swiss Air flight at the airport, go to the Swiss Air check-in desk or the customer service desk.\n\nStep 2: Provide your Flight Details\n\nProvide your flight details to the representative at the desk, including your booking reference number, flight number, and departure date. The representative will confirm your flight details and ask you why you want to cancel your flight.\n\nStep 3: Confirm the Cancellation\n\nConfirm that you want to cancel your flight. The representative will let you know if there are any cancellation fees or penalties associated with your ticket, and what your refund options are.\n\nStep 4: Receive Confirmation\n\nYou will receive a confirmation email once your cancellation has been processed. Make sure to save this email for your records.\n\nImportant Things to Keep in Mind to Cancel a Swiss Air Flight\nIf you have a non-refundable ticket, you may not be eligible for a refund or may only be able to receive a partial refund.\nIf you booked your flight through a third-party website or travel agent, you may need to contact them directly to cancel your flight.\nAlways check the terms and conditions of your ticket to make sure you understand the cancellation policy and any associated fees or penalties.\nIf you\'re cancelling your flight due to unforeseen circumstances such as a medical emergency or a natural disaster, Swiss Air may offer you special exemptions or accommodations.\nWhat is Swiss Airlines 24 Hour Cancellation Policy?\nSwiss Airlines has a 24 hour cancellation policy that allows passengers to cancel their flights within 24 hours of booking at +1-877-507-7341 without penalty. This policy applies to all fare types, including non-refundable tickets. If you cancel your Swiss Airlines flight within 24 hours of booking, you\'ll receive a full refund of your ticket price.\n\nHow to Cancel Swiss Airlines Flight within 24 Hours?\nIf you need to cancel your Swiss Airlines flight within 24 hours of booking, you can do so easily online. Here are the steps to follow:\n\nGo to Swiss Airlines\' website and click on the "Manage your bookings" tab.\nEnter your booking reference number and last name to access your booking.\nSelect the flight you want to cancel and click on "Cancel flight."\nConfirm your cancellation and you\'ll receive a full refund of your ticket price.\nIf you booked your Swiss Airlines flight through a travel agent, you\'ll need to contact them directly to cancel your flight within 24 hours.\n\nImportant Things to Keep in Mind for Swiss Airlines 24 Hour Cancellation\nHere are some important things to keep in mind when cancelling your Swiss Airlines flight within 24 hours:\n\nSwiss Airlines\' 24 hour cancellation policy only applies to flights booked directly through Swiss Airlines. If you booked your flight through a travel agent or third-party website, you\'ll need to check their cancellation policy.\nIf you cancel your Swiss Airlines flight after the 24 hour window, you may be subject to cancellation fees or penalties.\nIf you have a non-refundable ticket and cancel your flight within 24 hours of booking, you\'ll receive a full refund of your ticket price. However, if you cancel your flight after the 24 hour window, you may not be eligible for a refund.\nSwiss Airlines\' 24 hour cancellation policy allows passengers to cancel their flights within 24 hours of booking without penalty. If you need to cancel your Swiss Airlines flight within 24 hours, you can do so easily online. Just remember to check the terms and conditions of your ticket to make sure you\'re eligible for a refund.\n\nSwiss Air Cancellation Fees\nThe cancellation fees for Swiss Air flights may vary depending on the type of ticket you have purchased. The airline offers three different types of tickets, which are:\n\nFlex Ticket - This ticket offers the most flexibility and allows passengers to make changes or cancel their flight without incurring any additional fees.\nStandard Ticket - This ticket offers some flexibility but charges a fee for changes and cancellations. The fee for cancelling a standard ticket can range from 100 to 250 CHF, depending on the route and time of cancellation.\nEconomy Ticket - This ticket offers the least flexibility and charges a fee for any changes or cancellations. The fee for cancelling an economy ticket can range from 150 to 350 CHF, depending on the route and time of cancellation.\nIt is important to note that the fees listed above are subject to change and may vary depending on the specific ticket you have purchased. Additionally, if you have purchased any add-ons or upgrades, such as extra baggage or seat selection, the fees associated with cancelling those may also apply.\n\nSwiss Air Refund Policy\nIf you cancel your Swiss Air flight, you may be eligible for a refund depending on the type of ticket you have purchased and the time of cancellation. Here are the details:\n\nFlex Ticket - If you have purchased a Flex Ticket, you can cancel your flight without incurring any fees and receive a full refund.\nStandard Ticket - If you have purchased a Standard Ticket and cancel your flight within 24 hours of booking, you can receive a full refund. If you cancel your flight after 24 hours, you may be charged a cancellation fee and receive a partial refund.\nEconomy Ticket - If you have purchased an Economy Ticket and cancel your flight within 24 hours of booking, you can receive a full refund. If you cancel your flight after 24 hours, you may be charged a cancellation fee and receive a partial refund.\nIt is important to note that the refund policy may vary depending on the route and time of cancellation. Additionally, if you have purchased any add-ons or upgrades, the refund policy associated with those may also apply.\n\nSwiss Flight Cancellation Compensation Explained\nSwiss Air has a comprehensive cancellation policy that outlines the compensation passengers are entitled to in case of flight cancellations. Depending on the circumstances, passengers may be eligible for a full refund, rebooking on the next available flight, or financial compensation. We\'ll break down the specifics of the policy and provide step-by-step instructions on how to make a claim for compensation.\n\nIn addition, we\'ll also provide tips on how to avoid flight cancellations in the first place, such as booking your flight in advance and keeping an eye on weather forecasts and other potential disruptions.\n\nFlight cancellations can be frustrating, but knowing your rights and how to claim compensation can make the experience less stressful. With Swiss Air\'s comprehensive cancellation policy and our tips for avoiding cancellations, you can rest assured that your travel plans are in good hands.\n\nConclusion\n\nIn summary, the Swiss Air Cancellation Policy is designed to provide passengers with flexibility and options when it comes to cancelling their flights. If you need to cancel a Swiss Air flight, you can do so online, through the mobile app, or by contacting the Swiss Air Customer Service team. However, it is important to understand the fees associated with cancelling a flight and the refund policy that applies to your specific ticket.\n\nBy understanding the Swiss Air Cancellation Policy, you can make informed decisions and avoid any confusion or additional charges. With this policy, Swiss Airlines aims to provide flexibility and convenience to its passengers, making travel planning a hassle-free experience.\n\n',
        name='lookup_policy', id='895c10fd-d81f-4eb2-a3b0-9b98c5371932', tool_call_id='call_hazAV15Z2195h38XzHnLSwZT'),
        AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_LIu4oFOTAWzpbQQa8qRK9VMJ',
                                                                 'function': {
                                                                     'arguments': '{"departure_airport":"CDG","arrival_airport":"BSL","start_time":"2024-11-15T14:48:15.554238-04:00","end_time":"2024-11-16T23:59:59-04:00"}',
                                                                     'name': 'search_flights'},
                                                                 'type': 'function'}], 'refusal': None},
                  response_metadata={'token_usage': {'completion_tokens': 68, 'prompt_tokens': 4540,
                                                     'total_tokens': 4608,
                                                     'completion_tokens_details': {'audio_tokens': 0,
                                                                                   'reasoning_tokens': 0,
                                                                                   'accepted_prediction_tokens': 0,
                                                                                   'rejected_prediction_tokens': 0},
                                                     'prompt_tokens_details': {'audio_tokens': 0,
                                                                               'cached_tokens': 0}},
                                     'model_name': 'gpt-4-turbo-2024-04-09',
                                     'system_fingerprint': 'fp_d5d846896e', 'finish_reason': 'tool_calls',
                                     'logprobs': None}, id='run-05d73b4a-a102-4ab9-94b5-122f1028c6fb-0',
                  tool_calls=[{'name': 'search_flights',
                               'args': {'departure_airport': 'CDG', 'arrival_airport': 'BSL',
                                        'start_time': '2024-11-15T14:48:15.554238-04:00',
                                        'end_time': '2024-11-16T23:59:59-04:00'},
                               'id': 'call_LIu4oFOTAWzpbQQa8qRK9VMJ', 'type': 'tool_call'}],
                  usage_metadata={'input_tokens': 4540, 'output_tokens': 68, 'total_tokens': 4608,
                                  'input_token_details': {'audio': 0, 'cache_read': 0},
                                  'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(
        content='[{"flight_id": 19233, "flight_no": "LX0112", "scheduled_departure": "2024-11-16 14:48:15.554238-04:00", "scheduled_arrival": "2024-11-16 16:18:15.554238-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "On Time", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19250, "flight_no": "LX0112", "scheduled_departure": "2024-11-15 14:48:15.554238-04:00", "scheduled_arrival": "2024-11-15 16:18:15.554238-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "On Time", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}]',
        name='search_flights', id='5e493b2d-2652-4eb6-a17b-8b6ff74a611d', tool_call_id='call_LIu4oFOTAWzpbQQa8qRK9VMJ'),
        AIMessage(
            content='目前，我找到的能在今天晚些时候离开的航班是航班号LX0112，计划于2024年11月16日14:48从巴黎戴高乐机场出发，预计16:18到达巴塞尔机场。这是明天的航班，因为没有其他航班更晚些离开。如果您想改订到这个航班，我可以为您处理。请告诉我是否继续。',
            additional_kwargs={'refusal': None}, response_metadata={
                'token_usage': {'completion_tokens': 139, 'prompt_tokens': 4854, 'total_tokens': 4993,
                                'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                              'accepted_prediction_tokens': 0,
                                                              'rejected_prediction_tokens': 0},
                                'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
                'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_d5d846896e',
                'finish_reason': 'stop', 'logprobs': None},
            id='run-9c130af3-c326-4afa-a03d-327b6e43fc4a-0',
            usage_metadata={'input_tokens': 4854, 'output_tokens': 139, 'total_tokens': 4993,
                            'input_token_details': {'audio': 0, 'cache_read': 0},
                            'output_token_details': {'audio': 0, 'reasoning': 0}}),
        HumanMessage(content='那就把我的航班改到下周的某个时间吧。', additional_kwargs={},
                     response_metadata={}, id='b28560c0-084b-4b2c-8f82-758f6a8a3b67'),
        AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_fbSkyCezsvJFyQ6TjL5PRFVE',
                                                                 'function': {
                                                                     'arguments': '{"departure_airport":"CDG","arrival_airport":"BSL","start_time":"2024-11-16T00:00:00-04:00","end_time":"2024-11-22T23:59:59-04:00"}',
                                                                     'name': 'search_flights'},
                                                                 'type': 'function'}], 'refusal': None},
                  response_metadata={'token_usage': {'completion_tokens': 65, 'prompt_tokens': 5022,
                                                     'total_tokens': 5087,
                                                     'completion_tokens_details': {'audio_tokens': 0,
                                                                                   'reasoning_tokens': 0,
                                                                                   'accepted_prediction_tokens': 0,
                                                                                   'rejected_prediction_tokens': 0},
                                                     'prompt_tokens_details': {'audio_tokens': 0,
                                                                               'cached_tokens': 0}},
                                     'model_name': 'gpt-4-turbo-2024-04-09',
                                     'system_fingerprint': 'fp_d5d846896e', 'finish_reason': 'tool_calls',
                                     'logprobs': None}, id='run-b9cf32e0-82c4-4bb9-b9f7-8e5a94d4d297-0',
                  tool_calls=[{'name': 'search_flights',
                               'args': {'departure_airport': 'CDG', 'arrival_airport': 'BSL',
                                        'start_time': '2024-11-16T00:00:00-04:00',
                                        'end_time': '2024-11-22T23:59:59-04:00'},
                               'id': 'call_fbSkyCezsvJFyQ6TjL5PRFVE', 'type': 'tool_call'}],
                  usage_metadata={'input_tokens': 5022, 'output_tokens': 65, 'total_tokens': 5087,
                                  'input_token_details': {'audio': 0, 'cache_read': 0},
                                  'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(
        content='[{"flight_id": 19232, "flight_no": "LX0112", "scheduled_departure": "2024-11-19 14:48:15.554238-04:00", "scheduled_arrival": "2024-11-19 16:18:15.554238-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19233, "flight_no": "LX0112", "scheduled_departure": "2024-11-16 14:48:15.554238-04:00", "scheduled_arrival": "2024-11-16 16:18:15.554238-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "On Time", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19251, "flight_no": "LX0112", "scheduled_departure": "2024-11-22 14:48:15.554238-04:00", "scheduled_arrival": "2024-11-22 16:18:15.554238-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19252, "flight_no": "LX0112", "scheduled_departure": "2024-11-21 14:48:15.554238-04:00", "scheduled_arrival": "2024-11-21 16:18:15.554238-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19265, "flight_no": "LX0112", "scheduled_departure": "2024-11-18 14:48:15.554238-04:00", "scheduled_arrival": "2024-11-18 16:18:15.554238-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19284, "flight_no": "LX0112", "scheduled_departure": "2024-11-20 14:48:15.554238-04:00", "scheduled_arrival": "2024-11-20 16:18:15.554238-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19287, "flight_no": "LX0112", "scheduled_departure": "2024-11-17 14:48:15.554238-04:00", "scheduled_arrival": "2024-11-17 16:18:15.554238-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}]',
        name='search_flights', id='7753ab96-b416-4261-8874-92e871f3e476', tool_call_id='call_fbSkyCezsvJFyQ6TjL5PRFVE'),
        AIMessage(
            content='接下来的一周内，有以下几个航班选项从巴黎戴高乐机场（CDG）飞往巴塞尔机场（BSL）：\n\n1. 2024年11月17日，14:48出发，16:18到达\n2. 2024年11月18日，14:48出发，16:18到达\n3. 2024年11月19日，14:48出发，16:18到达\n4. 2024年11月20日，14:48出发，16:18到达\n5. 2024年11月21日，14:48出发，16:18到达\n6. 2024年11月22日，14:48出发，16:18到达\n\n请告诉我，您希望改签到哪一天的航班。',
            additional_kwargs={'refusal': None}, response_metadata={
                'token_usage': {'completion_tokens': 214, 'prompt_tokens': 5917, 'total_tokens': 6131,
                                'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                              'accepted_prediction_tokens': 0,
                                                              'rejected_prediction_tokens': 0},
                                'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
                'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_35090ec11f',
                'finish_reason': 'stop', 'logprobs': None},
            id='run-fd11a3ef-2ed0-47ad-a3de-6681bd3704ec-0',
            usage_metadata={'input_tokens': 5917, 'output_tokens': 214, 'total_tokens': 6131,
                            'input_token_details': {'audio': 0, 'cache_read': 0},
                            'output_token_details': {'audio': 0, 'reasoning': 0}}),
        HumanMessage(content='下一个可选的时间很好。', additional_kwargs={}, response_metadata={},
                     id='61b9724d-913f-4217-88cb-b4728f8ae772'), AIMessage(content='', additional_kwargs={
        'tool_calls': [{'id': 'call_plc8gjxPub8vXJvt1RoyhGfv', 'function': {
            'arguments': '{"request":"Please change the flight LX0112 scheduled on 2024-11-15 to the flight on 2024-11-17 departing at 14:48 from CDG and arriving at 16:18 at BSL, for ticket number 7240005432906569."}',
            'name': 'ToFlightBookingAssistant'}, 'type': 'function'}], 'refusal': None}, response_metadata={
        'token_usage': {'completion_tokens': 73, 'prompt_tokens': 6148, 'total_tokens': 6221,
                        'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                      'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0},
                        'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
        'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_d5d846896e', 'finish_reason': 'tool_calls',
        'logprobs': None}, id='run-59df8648-f797-4382-89bb-025881e8d808-0', tool_calls=[
        {'name': 'ToFlightBookingAssistant', 'args': {
            'request': 'Please change the flight LX0112 scheduled on 2024-11-15 to the flight on 2024-11-17 departing at 14:48 from CDG and arriving at 16:18 at BSL, for ticket number 7240005432906569.'},
         'id': 'call_plc8gjxPub8vXJvt1RoyhGfv', 'type': 'tool_call'}], usage_metadata={'input_tokens': 6148,
                                                                                       'output_tokens': 73,
                                                                                       'total_tokens': 6221,
                                                                                       'input_token_details': {
                                                                                           'audio': 0, 'cache_read': 0},
                                                                                       'output_token_details': {
                                                                                           'audio': 0,
                                                                                           'reasoning': 0}}),
        ToolMessage(
            content="The assistant is now the Flight Updates & Booking Assistant. Reflect on the above conversation between the host assistant and the user. The user's intent is unsatisfied. Use the provided tools to assist the user. Remember, you are Flight Updates & Booking Assistant, and the booking, update, other other action is not complete until after you have successfully invoked the appropriate tool. If the user changes their mind or needs help for other tasks, call the CompleteOrEscalate function to let the primary host assistant take control. Do not mention who you are - just act as the proxy for the assistant.",
            id='772ed393-f966-430f-9fa1-be37c3b97613', tool_call_id='call_plc8gjxPub8vXJvt1RoyhGfv'),
        AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_PPRJH5PCPF4eHS8zdkyikB5y',
                                                                 'function': {
                                                                     'arguments': '{"ticket_no":"7240005432906569","new_flight_id":19287}',
                                                                     'name': 'update_ticket_to_new_flight'},
                                                                 'type': 'function'}], 'refusal': None},
                  response_metadata={'token_usage': {'completion_tokens': 30, 'prompt_tokens': 6065,
                                                     'total_tokens': 6095,
                                                     'completion_tokens_details': {'audio_tokens': 0,
                                                                                   'reasoning_tokens': 0,
                                                                                   'accepted_prediction_tokens': 0,
                                                                                   'rejected_prediction_tokens': 0},
                                                     'prompt_tokens_details': {'audio_tokens': 0,
                                                                               'cached_tokens': 0}},
                                     'model_name': 'gpt-4-turbo-2024-04-09',
                                     'system_fingerprint': 'fp_5db30363ff', 'finish_reason': 'tool_calls',
                                     'logprobs': None}, id='run-c630e503-8016-4e08-9a5a-a32b4fa71cb0-0',
                  tool_calls=[{'name': 'update_ticket_to_new_flight',
                               'args': {'ticket_no': '7240005432906569', 'new_flight_id': 19287},
                               'id': 'call_PPRJH5PCPF4eHS8zdkyikB5y', 'type': 'tool_call'}],
                  usage_metadata={'input_tokens': 6065, 'output_tokens': 30, 'total_tokens': 6095,
                                  'input_token_details': {'audio': 0, 'cache_read': 0},
                                  'output_token_details': {'audio': 0, 'reasoning': 0}}),
        ToolMessage(content='Ticket successfully updated to new flight.',
                    name='update_ticket_to_new_flight', id='42202484-ca1a-4c6b-a59d-eb2c573e7ce1',
                    tool_call_id='call_PPRJH5PCPF4eHS8zdkyikB5y'), AIMessage(
        content='您的航班已成功更改为2024年11月17日从巴黎戴高乐机场（CDG）出发，14:48起飞，预计16:18到达巴塞尔机场（BSL）。请按时到达机场，并注意航班动态。祝您旅途愉快！如果需要其他帮助，请告诉我。',
        additional_kwargs={'refusal': None}, response_metadata={
            'token_usage': {'completion_tokens': 104, 'prompt_tokens': 6113, 'total_tokens': 6217,
                            'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                          'accepted_prediction_tokens': 0,
                                                          'rejected_prediction_tokens': 0},
                            'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
            'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_5db30363ff', 'finish_reason': 'stop',
            'logprobs': None}, id='run-03726c75-4289-4e40-9f1d-c5081c694a68-0',
        usage_metadata={'input_tokens': 6113, 'output_tokens': 104, 'total_tokens': 6217,
                        'input_token_details': {'audio': 0, 'cache_read': 0},
                        'output_token_details': {'audio': 0, 'reasoning': 0}}),
        HumanMessage(content='住宿和交通怎么办？', additional_kwargs={}, response_metadata={},
                     id='165e07e5-7983-40f1-b1bd-14de12d8a0fe'), AIMessage(content='', additional_kwargs={
        'tool_calls': [{'id': 'call_vTyGl1p8EFAhWQeyfA7NRczr', 'function': {
            'arguments': '{"reason":"The user is asking for assistance with accommodation and transportation, which are outside of my specialized function for handling flight updates and bookings. Escalating to the main assistant for further support."}',
            'name': 'CompleteOrEscalate'}, 'type': 'function'}], 'refusal': None}, response_metadata={
        'token_usage': {'completion_tokens': 52, 'prompt_tokens': 6109, 'total_tokens': 6161,
                        'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                      'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0},
                        'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
        'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_d5d846896e', 'finish_reason': 'tool_calls',
        'logprobs': None}, id='run-2fb8ad72-f397-4f68-b8a0-7ee468e77b75-0', tool_calls=[{'name': 'CompleteOrEscalate',
                                                                                         'args': {
                                                                                             'reason': 'The user is asking for assistance with accommodation and transportation, which are outside of my specialized function for handling flight updates and bookings. Escalating to the main assistant for further support.'},
                                                                                         'id': 'call_vTyGl1p8EFAhWQeyfA7NRczr',
                                                                                         'type': 'tool_call'}],
                                                                           usage_metadata={
                                                                               'input_tokens': 6109,
                                                                               'output_tokens': 52,
                                                                               'total_tokens': 6161,
                                                                               'input_token_details': {
                                                                                   'audio': 0,
                                                                                   'cache_read': 0},
                                                                               'output_token_details': {
                                                                                   'audio': 0,
                                                                                   'reasoning': 0}}),
        ToolMessage(
            content='Resuming dialog with the host assistant. Please reflect on the past conversation and assist the user as needed.',
            id='40b6be39-b296-485a-a9f9-cbf14ec498e9', tool_call_id='call_vTyGl1p8EFAhWQeyfA7NRczr'),
        AIMessage(
            content='我可以帮助您预订巴塞尔的住宿和交通。请提供您的入住日期和退房日期，以及您是否需要在巴塞尔租车的详细信息。如果您有特别的要求或偏好，请告诉我。这样我就可以更准确地为您安排。',
            additional_kwargs={'refusal': None}, response_metadata={
                'token_usage': {'completion_tokens': 93, 'prompt_tokens': 6478, 'total_tokens': 6571,
                                'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                              'accepted_prediction_tokens': 0,
                                                              'rejected_prediction_tokens': 0},
                                'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
                'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_d5d846896e',
                'finish_reason': 'stop', 'logprobs': None},
            id='run-315a6684-c08a-4f45-8f22-8340d0159c25-0',
            usage_metadata={'input_tokens': 6478, 'output_tokens': 93, 'total_tokens': 6571,
                            'input_token_details': {'audio': 0, 'cache_read': 0},
                            'output_token_details': {'audio': 0, 'reasoning': 0}}),
        HumanMessage(content='是的，我想找一个价格适中的酒店，住一个星期（7天）。我还想租一辆车。',
                     additional_kwargs={}, response_metadata={},
                     id='77ccc6b1-d225-4cc2-92cd-c005e4f5cf74'), AIMessage(content='', additional_kwargs={
        'tool_calls': [{'id': 'call_KMj8JDSwpLoerNSmWiCcpIsx', 'function': {
            'arguments': '{"location": "Basel", "checkin_date": "2024-11-17", "checkout_date": "2024-11-24", "request": "Please book a mid-priced hotel for 7 nights."}',
            'name': 'ToHotelBookingAssistant'}, 'type': 'function'}, {'id': 'call_HQs3ZXIYA3PjqMxDd9bSB8Kx',
                                                                      'function': {
                                                                          'arguments': '{"location": "Basel", "start_date": "2024-11-17", "end_date": "2024-11-24", "request": "Please arrange a car rental for the duration of the stay."}',
                                                                          'name': 'ToBookCarRental'},
                                                                      'type': 'function'}], 'refusal': None},
                                                                           response_metadata={
                                                                               'token_usage': {
                                                                                   'completion_tokens': 120,
                                                                                   'prompt_tokens': 6616,
                                                                                   'total_tokens': 6736,
                                                                                   'completion_tokens_details': {
                                                                                       'audio_tokens': 0,
                                                                                       'reasoning_tokens': 0,
                                                                                       'accepted_prediction_tokens': 0,
                                                                                       'rejected_prediction_tokens': 0},
                                                                                   'prompt_tokens_details': {
                                                                                       'audio_tokens': 0,
                                                                                       'cached_tokens': 0}},
                                                                               'model_name': 'gpt-4-turbo-2024-04-09',
                                                                               'system_fingerprint': 'fp_d5d846896e',
                                                                               'finish_reason': 'tool_calls',
                                                                               'logprobs': None},
                                                                           id='run-dc5004b5-b410-4866-a9f1-f97a9b4991c0-0',
                                                                           tool_calls=[{
                                                                               'name': 'ToHotelBookingAssistant',
                                                                               'args': {
                                                                                   'location': 'Basel',
                                                                                   'checkin_date': '2024-11-17',
                                                                                   'checkout_date': '2024-11-24',
                                                                                   'request': 'Please book a mid-priced hotel for 7 nights.'},
                                                                               'id': 'call_KMj8JDSwpLoerNSmWiCcpIsx',
                                                                               'type': 'tool_call'},
                                                                               {
                                                                                   'name': 'ToBookCarRental',
                                                                                   'args': {
                                                                                       'location': 'Basel',
                                                                                       'start_date': '2024-11-17',
                                                                                       'end_date': '2024-11-24',
                                                                                       'request': 'Please arrange a car rental for the duration of the stay.'},
                                                                                   'id': 'call_HQs3ZXIYA3PjqMxDd9bSB8Kx',
                                                                                   'type': 'tool_call'}],
                                                                           usage_metadata={
                                                                               'input_tokens': 6616,
                                                                               'output_tokens': 120,
                                                                               'total_tokens': 6736,
                                                                               'input_token_details': {
                                                                                   'audio': 0,
                                                                                   'cache_read': 0},
                                                                               'output_token_details': {
                                                                                   'audio': 0,
                                                                                   'reasoning': 0}}),
        ToolMessage(
            content="The assistant is now the Hotel Booking Assistant. Reflect on the above conversation between the host assistant and the user. The user's intent is unsatisfied. Use the provided tools to assist the user. Remember, you are Hotel Booking Assistant, and the booking, update, other other action is not complete until after you have successfully invoked the appropriate tool. If the user changes their mind or needs help for other tasks, call the CompleteOrEscalate function to let the primary host assistant take control. Do not mention who you are - just act as the proxy for the assistant.",
            id='c4f7b3fa-0287-47ce-a5f7-a0d157afdb8d', tool_call_id='call_KMj8JDSwpLoerNSmWiCcpIsx')],
    'user_info': [], 'dialog_state': ['book_hotel']}
