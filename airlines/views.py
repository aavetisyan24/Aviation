from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
import datetime
from .static import flight_search, final_airport_list


# def customers(a=0):
#     lst1 = [0, 1, 2, 3, 4]
#     maximumadult = list(range(1, 10))
#     maxchild = list(range(9))
#     maxinf = list(range(6))
#     if a in lst1:
#         maxchild=list(range(6))
#         maxinf=a
#     elif a not in lst1:
#         maxinf=list(range(6))
#         maxchild = list(range(10 - a))
#     print(maximumadult, maxchild, maxinf)
#     return [maximumadult, maxchild, maxinf]


# Create your views here.
def search(request):
    global infant, child, adult
    airport = final_airport_list.airport_list
    today = str(datetime.date.today())
    next_year = f"{str(datetime.date.today().year + 1)}-{str(datetime.date.today().month)}-{str(datetime.date.today().day)}"
    return render(request, "airlines/search.html", {"airport": airport, "today": today, "next_year": next_year,
                                                    })


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
    print("stopover", stopover)
    adults = request.GET["adult"]
    childs = request.GET["child"]
    infants = request.GET["infant"]
    print("adults-childs-infants", adults, childs, infants)
    return render(request, "airlines/search_result.html",
                  {"search_result": flight_search.flt_search(origin, destination, day_origin, day_return, adults=adults,
                                                             stopover=stopover, chd=childs, inf=infants),
                   "origin": origin1[6:],
                   "destination": destination1[6:],
                   "date": day_origin,
                   "date_return": day_return,
                   "chd": childs,
                   "inf": infants})
