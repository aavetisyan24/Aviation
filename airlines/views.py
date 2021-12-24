from django.shortcuts import render
from django.http import HttpResponse
from .static import flight_search, final_airport_list
import datetime
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def search(request):
    airport = final_airport_list.airport_list
    today = str(datetime.date.today())
    next_year = f"{str(datetime.date.today().year + 1)}-{str(datetime.date.today().month)}-{str(datetime.date.today().day)}"
    return render(request, "airlines/search.html", {"airport": airport, "today": today, "next_year": next_year})

def search_result(request):
    origin1 = request.GET["origin"]
    print(origin1)
    origin = (origin1)[:3]
    destination1 = request.GET['destination']
    print(destination1)
    destination = (destination1)[:3]
    day_origin = request.GET['day_origin']
    day_return = request.GET['day_return']
    if day_return:
        print("day return available")
    else:
        print("day return not available")
    print(day_origin, "-", day_return)
    try:
        stopover = request.GET['stopover']
    except MultiValueDictKeyError:
        stopover = "false"
    print(stopover)
    return render(request, "airlines/search_result.html",
                  {"search_result": flight_search.flt_search(origin, destination, day_origin, day_return, stopover),
                   "origin": origin1[6:],
                   "destination": destination1[6:],
                   "date": day_origin,
                   "date_return": day_return})
