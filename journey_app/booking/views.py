from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def booking_page(client):
    return HttpResponse("Hi, " % question_id % ", you can book here  ")