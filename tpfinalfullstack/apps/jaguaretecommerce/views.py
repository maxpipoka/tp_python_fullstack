from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def blog(request):
    return HttpResponse("Texto plano")

def inicio(request):
    return render(request, 'index.html')