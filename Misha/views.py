from django.shortcuts import render
from django.http import HttpResponse

def example(request):
    return HttpResponse("WELCOME TO THE WEBSITE")
def home(request):
    return HttpResponse("WELCOME TO THE HOME PAGE")
def summa(request, a, b):
    return HttpResponse(f"Сумма чисел {a} и {b} равна {a + b}")
def html(request):
    return render(request, 'html.html')