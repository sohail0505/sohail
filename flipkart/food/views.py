from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nonveg(request):
    return HttpResponse('<h1>nonveg is spicy food and tasty food</h1>')
