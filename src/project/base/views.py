from django.shortcuts import render
from django.http import HttpResponse

def to_do_list(request):
    return HttpResponse("Hello, world. This is the to do list.")
