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

state = {'messages': [
    HumanMessage(content='Hi there, what time is my flight?', additional_kwargs={}, response_metadata={},
                 id='3c85ef33-ab81-47e2-a16f-b948331bec22'),
    AIMessage(
        content='Your flight, LX0112, is scheduled to depart from Paris Charles de Gaulle Airport (CDG) today at **15:55** and will arrive at Basel Airport (BSL) at **17:25**. Please make sure to be at the gate on time for boarding.',
        additional_kwargs={'refusal': None}, response_metadata={
            'token_usage': {'completion_tokens': 60, 'prompt_tokens': 880, 'total_tokens': 940,
                            'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                          'accepted_prediction_tokens': 0,
                                                          'rejected_prediction_tokens': 0},
                            'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
            'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_d5d846896e', 'finish_reason': 'stop',
            'logprobs': None}, id='run-bf402040-9ac1-4a49-a633-37035b473aae-0',
        usage_metadata={'input_tokens': 880, 'output_tokens': 60, 'total_tokens': 940,
                        'input_token_details': {'audio': 0, 'cache_read': 0},
                        'output_token_details': {'audio': 0, 'reasoning': 0}}),
    HumanMessage(content='Am i allowed to update my flight to something sooner? I want to leave later today.',
                 additional_kwargs={}, response_metadata={}, id='24cdbc1e-72af-4dc4-80ec-6203de42bd33'),
    AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_8FL9Brtpty43CosfriIBmM1B', 'function': {
        'arguments': '{"query":"flight change policy for economy tickets"}', 'name': 'lookup_policy'},
                                                             'type': 'function'}], 'refusal': None}, response_metadata={
        'token_usage': {'completion_tokens': 19, 'prompt_tokens': 965, 'total_tokens': 984,
                        'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                      'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0},
                        'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
        'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_d5d846896e', 'finish_reason': 'tool_calls',
        'logprobs': None}, id='run-26b88982-318c-4298-9470-71504e27179c-0', tool_calls=[
        {'name': 'lookup_policy', 'args': {'query': 'flight change policy for economy tickets'},
         'id': 'call_8FL9Brtpty43CosfriIBmM1B', 'type': 'tool_call'}],
              usage_metadata={'input_tokens': 965, 'output_tokens': 19, 'total_tokens': 984,
                              'input_token_details': {'audio': 0, 'cache_read': 0},
                              'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(
        content='\n## Frequently asked questions: European fare concept\nCan a particular Economy fare be fully booked?\nNo. As long as there are still seats in Economy Class, all three Economy fares will always be available in every available booking class .\n\nCan the SWISS fares be booked on codeshare flights operated by other airlines? What happens when changing a flight from a SWISS-operated flight to a codeshare flight (e.g. Zurich-Lisbon with TAP Portugal)?\nThe fares Economy Classic, Economy Flex and Business can be booked on codeshare flights. Economy Light can only be booked on flights operated by SWISS (airline code LX). For technical reasons, seats cannot be reserved on codeshare flights for the time being.\n\nWhy doesn\'t SWISS offer an Economy Flex fare for groups?\nGroup bookings can be changed to any fare option free of charge until the time the ticket is issued provided that the same price is still available. The Economy Flex fare therefore does not provide an additional benefit for groups, and so we do not offer it.\n\nCan the additional options (advance seat reservation, additional baggage etc.) always be changed?\nThe additional options cannot be rebooked with Economy Light because the fare itself cannot be changed. With the Economy Classic fare, the additional options can only be booked on the same reservation.\n\nIs it possible to pay for an upgrade to Business Class with the Economy Light, Economy Classic and Economy Flex fares?\nWenn Sie einen Tarif Economy Light, Economy Classic oder Economy Flex gebucht haben, können Sie ein Upgrade in die Business Class buchen, das viele Leistungen der Business Class enthält. Es ist via swiss.com oder dem SWISS Service Center buchbar.\n\nWhat do status customers (HON Circle Member, Senator, Frequent Traveller) need to consider when choosing a fare?\nTarif Economy Light does not include free advanced seat reservation or any additional baggage (e.g. golf equipment). All other status benefits, such as free lounge access, remain unchanged with this fare.\n\nWhat do SWISS Golf Traveller Club members need to consider when choosing a fare?\nIm Tarif Economy Light ist keine kostenlose Mitnahme von Golfgepäck möglich.\n\nWhat are the differences in the miles credits with the various fares?\nThe number of miles credited is still determined by the booking class.\n\nIf I have booked a Light fare and paid for an additional item of baggage and then cancel my flight, do I lose everything?\nLike the Ecnomy Light fare, the charge for the first item of paid baggage will not be reimbursed, nor can it be used for a different flight.\n\nIf I book an Economy Classic fare and travel without checked baggage, will I be reimbursed for the baggage not taken?\nNo; no refunds are given for any services included in a fare that are not used.\n\nWhat is the difference between the 1 st bag and the additional bag?\nThe 1 st bag can only be purchased with the Economy Light fare. It costs less than the additional item of baggage.\n\nWith the Economy Light fare, how can I purchase a 1 st bag (max. 23 kg) in addition?\nThe first 1 st bag in the Economy Light fare can be purchased through your travel agent, through swiss.com (up to 6 hours before departure), the SWISS Service Center (up to 24 hours before departure) or at the airport. The price at the airport will be higher than for purchasing in advance. The charge is due for each flight route.\n\nIf I am asked at the gate to check in my baggage, can I quickly purchase it online in order to benefit from the lower price?\nNo; you can only purchase it via swiss.com up to1 hour before departure. Different prices apply at the airport.\n\nHow many additional items of baggage can I purchase?\nYou can purchase a maximum of two additional items of baggage via swiss.com. If you are going through a travel agent, you can purchase a maximum of one 1 st bag plus one additional bag.if you go through the SWISS Service Center, there is no limit to the number of additional items of baggage you may purchase.\n\nSWISS Economy Flex: what does the “Change to earlier flight on the same day” service offer?\nApplies to "Economy Flex" and "Business Flex" fares. Rebooking free of charge is possible only on the day of departure during online check-in via lufthansa.com or the Lufthansa app, or at a check-in machine or check-in counter at the airport. Applies to direct flights only. A change of route or airline is not possible.\n\n\n\n\n\n## Booking and Cancellation\n\n1. How can I change my booking?\n\t* The ticket number must start with 724 (SWISS ticket no./plate).\n\t* The ticket was not paid for by barter or voucher (there are exceptions to voucher payments; if the ticket was paid for in full by voucher, then it may be possible to rebook online under certain circumstances. If it is not possible to rebook online because of the payment method, then you will be informed accordingly during the rebooking process).\n\t* There must be an active flight booking for your ticket. It is not possible to rebook open tickets or tickets without the corresponding flight segments online at the moment.\n\t* It is currently only possible to rebook outbound (one-way) tickets or return tickets with single flight routes (point-to-point).\n2. Which tickets/bookings cannot be rebooked online currently?\n\t* Bookings containing flight segments with other airlines\n\t* Bookings containing reservations, where a ticket has not yet been issued\n\t* Bookings with several valid tickets for the same person and route\n\t* Tickets with a status other than O (open) (A)\n\t* Bookings with segments with a status other than OK (e.g. containing flight segments with the status Waitlist) (HK|RR)\n\t* Tickets that do not display the tariff calculation (IT tickets)\n\t* Bookings that contain special services (e.g. transportation of animals/transportation of medical equipment/transportation of special sporting equipment etc.)\n\t* Tickets that are part of a group booking\n\t* Tickets on which the booking class (RBD) does not correspond to the tariff code (FareBase)\n3. Am I allowed to make changes to my online redemption booking?\n\t* Redemption bookings can not yet be changed on swiss.com.\n4. What changes can I make on my ticket?\n\t* You can change the flight and the travel dates. Change of origin and destination or name changes are not possible online.\n5. After I have made changes to the itinerary online, can I make another change?\n\t* If the fare condition allows it, it is possible to make multiple changes to the itinerary.\n6. Can a name be changed after a booking is made?\n\t* The correct name(s) of the customer travelling need to be entered in a booking. The first and last name of the passenger travelling needs to be entered exactly as in the travel documents. Entering a middle name is optional and can be added in the first name field. However, there is a character limitation for this field.\n\t* Your first and middle name is stored by the system spelled together without spaces. This is not a mistake and does not affect your booking.\n\t* Any subsequent name changes, including adding names to a ticket, are not allowed.\n7. Is it possible to apply the changes only to some of the passengers in the same booking?\n\t* The changes will always be applied to all passengers travelling together. Changes to the passenger name or number of passengers is not possible online.\n8. Until what time before departure can a flight be rebooked online?\n\t* The minimum time before departure for online rebookings depends on your departure airport. If you are departing from a Swiss airport, then you can rebook online up to three hours before departure.\n9. Will any differences in airport taxes be refunded online, if the new flight choice is cheaper?\n\t* No, online refunds are currently not possible.\n10. Why isn\'t the rebooking made in the same currency as the ticket?\n\t* Any calculations associated with the rebooking will be made in the currency of the original country of departure (Point of Commencement).\n11. Will my seat reservation be taken into account in the rebooking?\n\t* Yes, your seat reservation will be included in the rebooking.\n12. Will my special meal be included in the rebooking?\n\t* Yes, your special meal will be included.\n13. Will my additional passenger details (APIS) be included in the rebooking?\n\t* Yes, your APIS details will be included.\n14. Will the travel insurance obtained from the Europäische Reiseversicherung (European Travel Insurance) through SWISS be included in the new ticket?\n\t* Yes, the travel insurance obtained through SWISS will be included in the new ticket and will remain valid.\n15. Will I be given a new booking reference after rebooking?\n\t* No, your booking reference will stay the same after rebooking.\n16. Will I be given a new ticket number after rebooking?\n\t* Yes, you will be given a new ticket number after rebooking.\n17. Can I change my booking after checking in online?\n\t* No, only tickets with the status "Open" can be changed online.\n18. I want to change a flight booking which is part of a package purchased with a Travel Agency. What do I need to consider?\n\t* The changes processed on swiss.com are limited to the flight booking only. No changes to any other service included in your package (e.g. hotel, rental car etc.) will be processed.\n19. I want to process an online change to a flight booking which was purchased with a Travel Agency. What do I need to consider?\n\t* You can change your flight booking online, but your Travel Agency will not have access to your new electronic ticket.\n\n\n',
        name='lookup_policy', id='7ad66fee-c1d2-4359-a54c-87899430f4f2', tool_call_id='call_8FL9Brtpty43CosfriIBmM1B'),
    AIMessage(
        content="Yes, you are allowed to update your flight to a different time today, provided that it is available and you are booked under the Economy Flex fare. You can make this change online through the Swiss Airlines website or app, or at the airport's check-in counters and self-service kiosks.\n\nWould you like me to proceed with finding an available flight for you departing later today from Paris to Basel?",
        additional_kwargs={'refusal': None}, response_metadata={
            'token_usage': {'completion_tokens': 81, 'prompt_tokens': 3027, 'total_tokens': 3108,
                            'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                          'accepted_prediction_tokens': 0,
                                                          'rejected_prediction_tokens': 0},
                            'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
            'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_d5d846896e', 'finish_reason': 'stop',
            'logprobs': None}, id='run-94c6dbe3-0441-4b06-9bff-cacabc443904-0',
        usage_metadata={'input_tokens': 3027, 'output_tokens': 81, 'total_tokens': 3108,
                        'input_token_details': {'audio': 0, 'cache_read': 0},
                        'output_token_details': {'audio': 0, 'reasoning': 0}}),
    HumanMessage(content='Update my flight to sometime next week then', additional_kwargs={}, response_metadata={},
                 id='ffbe046f-7a2b-4cd5-a090-7f020819dc32'), AIMessage(content='', additional_kwargs={'tool_calls': [
        {'id': 'call_aV70tIRWFUeU7ITWNdbde6IU', 'function': {
            'arguments': '{"request":"Update flight LX0112 from 2024-11-15 to a new date next week for ticket number 7240005432906569."}',
            'name': 'ToFlightBookingAssistant'}, 'type': 'function'}], 'refusal': None}, response_metadata={
        'token_usage': {'completion_tokens': 45, 'prompt_tokens': 3123, 'total_tokens': 3168,
                        'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                      'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0},
                        'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
        'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_5db30363ff', 'finish_reason': 'tool_calls',
        'logprobs': None}, id='run-04a383a0-26c9-4801-aedc-3090bf981fca-0', tool_calls=[
        {'name': 'ToFlightBookingAssistant', 'args': {
            'request': 'Update flight LX0112 from 2024-11-15 to a new date next week for ticket number 7240005432906569.'},
         'id': 'call_aV70tIRWFUeU7ITWNdbde6IU', 'type': 'tool_call'}], usage_metadata={'input_tokens': 3123,
                                                                                       'output_tokens': 45,
                                                                                       'total_tokens': 3168,
                                                                                       'input_token_details': {
                                                                                           'audio': 0, 'cache_read': 0},
                                                                                       'output_token_details': {
                                                                                           'audio': 0,
                                                                                           'reasoning': 0}}),
    ToolMessage(
        content="The assistant is now the Flight Updates & Booking Assistant. Reflect on the above conversation between the host assistant and the user. The user's intent is unsatisfied. Use the provided tools to assist the user. Remember, you are Flight Updates & Booking Assistant, and the booking, update, other other action is not complete until after you have successfully invoked the appropriate tool. If the user changes their mind or needs help for other tasks, call the CompleteOrEscalate function to let the primary host assistant take control. Do not mention who you are - just act as the proxy for the assistant.",
        id='02daa143-bba2-4cf7-8068-0db57d4760fc', tool_call_id='call_aV70tIRWFUeU7ITWNdbde6IU'), AIMessage(content='',
                                                                                                            additional_kwargs={
                                                                                                                'tool_calls': [
                                                                                                                    {
                                                                                                                        'id': 'call_VY5TpHSOhh5sxaVjmiLsHOIi',
                                                                                                                        'function': {
                                                                                                                            'arguments': '{"departure_airport":"CDG","arrival_airport":"BSL","start_time":"2024-11-22","end_time":"2024-11-29"}',
                                                                                                                            'name': 'search_flights'},
                                                                                                                        'type': 'function'}],
                                                                                                                'refusal': None},
                                                                                                            response_metadata={
                                                                                                                'token_usage': {
                                                                                                                    'completion_tokens': 45,
                                                                                                                    'prompt_tokens': 3012,
                                                                                                                    'total_tokens': 3057,
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
                                                                                                            id='run-4f6caa71-ec0d-4611-843a-2cf803fd79b3-0',
                                                                                                            tool_calls=[
                                                                                                                {
                                                                                                                    'name': 'search_flights',
                                                                                                                    'args': {
                                                                                                                        'departure_airport': 'CDG',
                                                                                                                        'arrival_airport': 'BSL',
                                                                                                                        'start_time': '2024-11-22',
                                                                                                                        'end_time': '2024-11-29'},
                                                                                                                    'id': 'call_VY5TpHSOhh5sxaVjmiLsHOIi',
                                                                                                                    'type': 'tool_call'}],
                                                                                                            usage_metadata={
                                                                                                                'input_tokens': 3012,
                                                                                                                'output_tokens': 45,
                                                                                                                'total_tokens': 3057,
                                                                                                                'input_token_details': {
                                                                                                                    'audio': 0,
                                                                                                                    'cache_read': 0},
                                                                                                                'output_token_details': {
                                                                                                                    'audio': 0,
                                                                                                                    'reasoning': 0}}),
    ToolMessage(
        content='[{"flight_id": 19238, "flight_no": "LX0112", "scheduled_departure": "2024-11-23 15:55:44.314836-04:00", "scheduled_arrival": "2024-11-23 17:25:44.314836-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19242, "flight_no": "LX0112", "scheduled_departure": "2024-11-24 15:55:44.314836-04:00", "scheduled_arrival": "2024-11-24 17:25:44.314836-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19243, "flight_no": "LX0112", "scheduled_departure": "2024-11-26 15:55:44.314836-04:00", "scheduled_arrival": "2024-11-26 17:25:44.314836-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19249, "flight_no": "LX0112", "scheduled_departure": "2024-11-28 15:55:44.314836-04:00", "scheduled_arrival": "2024-11-28 17:25:44.314836-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19251, "flight_no": "LX0112", "scheduled_departure": "2024-11-22 15:55:44.314836-04:00", "scheduled_arrival": "2024-11-22 17:25:44.314836-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19259, "flight_no": "LX0112", "scheduled_departure": "2024-11-25 15:55:44.314836-04:00", "scheduled_arrival": "2024-11-25 17:25:44.314836-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19280, "flight_no": "LX0112", "scheduled_departure": "2024-11-27 15:55:44.314836-04:00", "scheduled_arrival": "2024-11-27 17:25:44.314836-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}]',
        name='search_flights', id='233d7552-bf35-4f2b-891b-56f1f9e0edc2', tool_call_id='call_VY5TpHSOhh5sxaVjmiLsHOIi'),
    AIMessage(
        content='Here are the available flights next week from Paris to Basel:\n\n1. **November 22, 2024**\n   - Departure: 15:55\n   - Arrival: 17:25\n\n2. **November 23, 2024**\n   - Departure: 15:55\n   - Arrival: 17:25\n\n3. **November 24, 2024**\n   - Departure: 15:55\n   - Arrival: 17:25\n\n4. **November 25, 2024**\n   - Departure: 15:55\n   - Arrival: 17:25\n\n5. **November 26, 2024**\n   - Departure: 15:55\n   - Arrival: 17:25\n\n6. **November 27, 2024**\n   - Departure: 15:55\n   - Arrival: 17:25\n\n7. **November 28, 2024**\n   - Departure: 15:55\n   - Arrival: 17:25\n\nPlease let me know which new date works best for you so I can update your ticket.',
        additional_kwargs={'refusal': None}, response_metadata={
            'token_usage': {'completion_tokens': 241, 'prompt_tokens': 3886, 'total_tokens': 4127,
                            'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                          'accepted_prediction_tokens': 0,
                                                          'rejected_prediction_tokens': 0},
                            'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
            'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_d5d846896e', 'finish_reason': 'stop',
            'logprobs': None}, id='run-d78f9cde-1e3a-4581-8a66-4528307fc4b2-0',
        usage_metadata={'input_tokens': 3886, 'output_tokens': 241, 'total_tokens': 4127,
                        'input_token_details': {'audio': 0, 'cache_read': 0},
                        'output_token_details': {'audio': 0, 'reasoning': 0}}),
    HumanMessage(content='The next available option is great', additional_kwargs={}, response_metadata={},
                 id='eb830afe-7735-4d7b-a40c-d9d178c4587c'), AIMessage(content='', additional_kwargs={'tool_calls': [
        {'id': 'call_ZGg65qCju73IuIbLnCU5YOQm',
         'function': {'arguments': '{"ticket_no":"7240005432906569","new_flight_id":19251}',
                      'name': 'update_ticket_to_new_flight'}, 'type': 'function'}], 'refusal': None},
                                                                       response_metadata={
                                                                           'token_usage': {'completion_tokens': 30,
                                                                                           'prompt_tokens': 4140,
                                                                                           'total_tokens': 4170,
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
                                                                       id='run-24935243-4359-4559-b3ba-3b01eef66fae-0',
                                                                       tool_calls=[
                                                                           {'name': 'update_ticket_to_new_flight',
                                                                            'args': {'ticket_no': '7240005432906569',
                                                                                     'new_flight_id': 19251},
                                                                            'id': 'call_ZGg65qCju73IuIbLnCU5YOQm',
                                                                            'type': 'tool_call'}],
                                                                       usage_metadata={'input_tokens': 4140,
                                                                                       'output_tokens': 30,
                                                                                       'total_tokens': 4170,
                                                                                       'input_token_details': {
                                                                                           'audio': 0, 'cache_read': 0},
                                                                                       'output_token_details': {
                                                                                           'audio': 0,
                                                                                           'reasoning': 0}}),
    ToolMessage(content='Ticket successfully updated to new flight.', name='update_ticket_to_new_flight',
                id='69ca9ef4-6db0-4cb9-976a-57a0186a4dde', tool_call_id='call_ZGg65qCju73IuIbLnCU5YOQm'), AIMessage(
        content='Your flight has been successfully updated. Here are the new details:\n\n- **Flight Number:** LX0112\n- **Departure:** November 22, 2024, at 15:55 from Paris Charles de Gaulle Airport (CDG)\n- **Arrival:** November 22, 2024, at 17:25 at Basel Airport (BSL)\n\nPlease let me know if there is anything else I can help you with! Safe travels!',
        additional_kwargs={'refusal': None}, response_metadata={
            'token_usage': {'completion_tokens': 95, 'prompt_tokens': 4188, 'total_tokens': 4283,
                            'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                          'accepted_prediction_tokens': 0,
                                                          'rejected_prediction_tokens': 0},
                            'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
            'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_d5d846896e', 'finish_reason': 'stop',
            'logprobs': None}, id='run-5d3e1fa0-567a-43f0-97fd-6f899add2098-0',
        usage_metadata={'input_tokens': 4188, 'output_tokens': 95, 'total_tokens': 4283,
                        'input_token_details': {'audio': 0, 'cache_read': 0},
                        'output_token_details': {'audio': 0, 'reasoning': 0}}),
    HumanMessage(content="OK cool so it's updated now?", additional_kwargs={}, response_metadata={},
                 id='b1b06904-8ca6-4af2-9e3c-c11c8e75b930'), AIMessage(
        content='Yes, your flight is updated now. You are all set with the new schedule departing on November 22, 2024. If you require any further assistance, feel free to ask! Safe travels!',
        additional_kwargs={'refusal': None}, response_metadata={
            'token_usage': {'completion_tokens': 42, 'prompt_tokens': 4170, 'total_tokens': 4212,
                            'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0,
                                                          'accepted_prediction_tokens': 0,
                                                          'rejected_prediction_tokens': 0},
                            'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
            'model_name': 'gpt-4-turbo-2024-04-09', 'system_fingerprint': 'fp_35090ec11f', 'finish_reason': 'stop',
            'logprobs': None}, id='run-f7efcb00-ff88-4cec-9242-d05781fb3ecf-0',
        usage_metadata={'input_tokens': 4170, 'output_tokens': 42, 'total_tokens': 4212,
                        'input_token_details': {'audio': 0, 'cache_read': 0},
                        'output_token_details': {'audio': 0, 'reasoning': 0}}),
    HumanMessage(content='Great - now i want to figure out lodging and transportation.', additional_kwargs={},
                 response_metadata={}, id='e369eb4c-6254-4467-82b3-a430cb4ab528'), AIMessage(content='',
                                                                                             additional_kwargs={
                                                                                                 'tool_calls': [{
                                                                                                     'id': 'call_TYnq8swnonGp2Mafy1NRi5fx',
                                                                                                     'function': {
                                                                                                         'arguments': '{"reason":"User requests assistance with lodging and transportation, which I cannot handle."}',
                                                                                                         'name': 'CompleteOrEscalate'},
                                                                                                     'type': 'function'}],
                                                                                                 'refusal': None},
                                                                                             response_metadata={
                                                                                                 'token_usage': {
                                                                                                     'completion_tokens': 29,
                                                                                                     'prompt_tokens': 4231,
                                                                                                     'total_tokens': 4260,
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
                                                                                             id='run-3dbf845b-4ddc-415b-b639-73a7e6c58d4e-0',
                                                                                             tool_calls=[{
                                                                                                 'name': 'CompleteOrEscalate',
                                                                                                 'args': {
                                                                                                     'reason': 'User requests assistance with lodging and transportation, which I cannot handle.'},
                                                                                                 'id': 'call_TYnq8swnonGp2Mafy1NRi5fx',
                                                                                                 'type': 'tool_call'}],
                                                                                             usage_metadata={
                                                                                                 'input_tokens': 4231,
                                                                                                 'output_tokens': 29,
                                                                                                 'total_tokens': 4260,
                                                                                                 'input_token_details': {
                                                                                                     'audio': 0,
                                                                                                     'cache_read': 0},
                                                                                                 'output_token_details': {
                                                                                                     'audio': 0,
                                                                                                     'reasoning': 0}}),
    ToolMessage(
        content='Resuming dialog with the host assistant. Please reflect on the past conversation and assist the user as needed.',
        id='1e39d7f8-0da6-4bce-bdb7-da1191b6718a', tool_call_id='call_TYnq8swnonGp2Mafy1NRi5fx'), AIMessage(content='',
                                                                                                            additional_kwargs={
                                                                                                                'tool_calls': [
                                                                                                                    {
                                                                                                                        'id': 'call_Vbbcs0YaX1FuszvMYjZW7rxv',
                                                                                                                        'function': {
                                                                                                                            'arguments': '{"location": "Basel", "start_date": "2024-11-22", "end_date": "2024-11-28", "request": "Please find a rental car available in Basel from November 22 to November 28."}',
                                                                                                                            'name': 'ToBookCarRental'},
                                                                                                                        'type': 'function'},
                                                                                                                    {
                                                                                                                        'id': 'call_eNs52weULc3aTqel4ujyq0Bg',
                                                                                                                        'function': {
                                                                                                                            'arguments': '{"location": "Basel", "checkin_date": "2024-11-22", "checkout_date": "2024-11-28", "request": "Please book a hotel in Basel from November 22 to November 28."}',
                                                                                                                            'name': 'ToHotelBookingAssistant'},
                                                                                                                        'type': 'function'}],
                                                                                                                'refusal': None},
                                                                                                            response_metadata={
                                                                                                                'token_usage': {
                                                                                                                    'completion_tokens': 129,
                                                                                                                    'prompt_tokens': 4577,
                                                                                                                    'total_tokens': 4706,
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
                                                                                                            id='run-edf7f5c1-0640-4228-b294-34536571db34-0',
                                                                                                            tool_calls=[
                                                                                                                {
                                                                                                                    'name': 'ToBookCarRental',
                                                                                                                    'args': {
                                                                                                                        'location': 'Basel',
                                                                                                                        'start_date': '2024-11-22',
                                                                                                                        'end_date': '2024-11-28',
                                                                                                                        'request': 'Please find a rental car available in Basel from November 22 to November 28.'},
                                                                                                                    'id': 'call_Vbbcs0YaX1FuszvMYjZW7rxv',
                                                                                                                    'type': 'tool_call'},
                                                                                                                {
                                                                                                                    'name': 'ToHotelBookingAssistant',
                                                                                                                    'args': {
                                                                                                                        'location': 'Basel',
                                                                                                                        'checkin_date': '2024-11-22',
                                                                                                                        'checkout_date': '2024-11-28',
                                                                                                                        'request': 'Please book a hotel in Basel from November 22 to November 28.'},
                                                                                                                    'id': 'call_eNs52weULc3aTqel4ujyq0Bg',
                                                                                                                    'type': 'tool_call'}],
                                                                                                            usage_metadata={
                                                                                                                'input_tokens': 4577,
                                                                                                                'output_tokens': 129,
                                                                                                                'total_tokens': 4706,
                                                                                                                'input_token_details': {
                                                                                                                    'audio': 0,
                                                                                                                    'cache_read': 0},
                                                                                                                'output_token_details': {
                                                                                                                    'audio': 0,
                                                                                                                    'reasoning': 0}}),
    ToolMessage(
        content="The assistant is now the Car Rental Assistant. Reflect on the above conversation between the host assistant and the user. The user's intent is unsatisfied. Use the provided tools to assist the user. Remember, you are Car Rental Assistant, and the booking, update, other other action is not complete until after you have successfully invoked the appropriate tool. If the user changes their mind or needs help for other tasks, call the CompleteOrEscalate function to let the primary host assistant take control. Do not mention who you are - just act as the proxy for the assistant.",
        id='5ac09f5b-7182-4897-96d5-c690e8ab5707', tool_call_id='call_Vbbcs0YaX1FuszvMYjZW7rxv')], 'user_info': [],
    'dialog_state': ['book_car_rental']}
