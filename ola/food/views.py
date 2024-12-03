from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def veg(request):
    return HttpResponse('This is Vegetarians Site')

def nonveg(request):
    return HttpResponse('This is non Vegetarians Site')

