from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

# def hello(request):
#     my_list = [1,2,3,4]
#     return HttpResponse(my_list)

# def hello(request):
#     body = """
#     <h1>Привет</h1>
#     <p>Параграф</p>
#     """   
#     return HttpResponse(body)



def hello(request):
    return HttpResponse("GeekTech", status=200, headers={"name": "Simon"})


def time(request):
    tim = datetime.datetime.now()
    return HttpResponse(tim)

def goodbye(request):
    return HttpResponse("Goodbye!")