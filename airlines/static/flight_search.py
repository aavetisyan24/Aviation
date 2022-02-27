from amadeus import Client, ResponseError
import pprint
from . import key

amadeus = Client(
    client_id=key.API_KEY,
    client_secret=key.API_SECRET
)


def flt_search(origin, destination, day_origin, day_return, stopover, max_flight_show=20, adults="",  chd="", inf="",):
    try:
        if day_return:
            print("return day is: ", day_return)
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin,
                destinationLocationCode=destination,
                departureDate=day_origin,
                returnDate=day_return,
                nonStop=stopover,
                max=max_flight_show,
                adults=adults,
                infants=inf,
                children=chd

            )
        else:
            print("one way flight")
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin,
                destinationLocationCode=destination,
                departureDate=day_origin,
                nonStop=stopover,
                max=max_flight_show,
                adults=adults,
                infants=1,
                children=1
            )
        message = response.data
        pprint.pprint(message)
        print(len(message))
        return message, origin, destination

    except ResponseError as error:
        return error

# def flt_search(origin, destination, day_origin, day_return=None, stopover=None):
#
#     try:
#         response = amadeus.shopping.flight_offers_search.get(
#             originLocationCode=origin,
#             destinationLocationCode=destination,
#             departureDate=day_origin,
#             returnDate=day_return,
#             adults=1,
#             max=3,
#             nonStop=stopover
#         )
#         message = response.data
#         pprint.pprint(message)
#         print(len(message))
#         return message, origin, destination
#
#     except ResponseError as error:
#         return error