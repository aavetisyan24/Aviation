from amadeus import Client, ResponseError
import pprint
import key

amadeus = Client(
    client_id=key.API_KEY,
    client_secret=key.API_SECRET
)

def flt_search(origin="JFK", destination="LAX", day_origin='2021-12-24', day_return='', stopover='true', max_flight_show=7, adults=1):
    try:
        if day_return:
            print("return day is: ",day_return)
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin,
                destinationLocationCode=destination,
                departureDate=day_origin,
                returnDate=day_return,
                adults=adults,
                max=max_flight_show,
                nonStop=stopover
            )
        else:
            print("one way flight")
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin,
                destinationLocationCode=destination,
                departureDate=day_origin,
                adults=adults,
                max=max_flight_show,
                nonStop=stopover
            )
        message = response.data
        pprint.pprint(message)
        print(len(message))
        return message, origin, destination

    except ResponseError as error:
        return error

flt_search()