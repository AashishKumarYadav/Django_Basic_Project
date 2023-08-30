from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'task.html',{'dynamic_data': 'Hello, dynamic data given By Aashish'})