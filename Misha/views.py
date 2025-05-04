from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Category,News
from .forms import Regform,LogForm
from django.contrib.auth import login,logout,authenticate
def example(request):
    return HttpResponse("WELCOME TO THE WEBSITE")
def home(request):
    return HttpResponse("WELCOME TO THE HOME PAGE")
def summa(request, a, b):
    return HttpResponse(f"Сумма чисел {a} и {b} равна {a + b}")
def html(request):
    return render(request, 'html.html')

def newslist(request):
    misha=News.objects.all()
    return render(request,'home.html',{'misha':misha})

def homepage(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context_menu = {
        'misha':news,
        'categories':categories,


    }
    return render(request,'home.html',context_menu)

def detail(request,id):
    novost = get_object_or_404(News,id=id)
    context = {
        'novost':novost

    }
    return render(request,'detail.html',context)


def category(request,id):
    category = Category.objects.all()
    news = News.objects.filter(category_id=id)

    context = {
        'categories':category,
        'news':news


    }
    return render(request,'category.html',context)


def reg(request):
    if request.method=='POST':
        form=Regform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=Regform()
    context={
        'form':form
    }
    return render(request,'REG.html',context)


def log_in(request):
    if request.method=='POST':
        form=LogForm(request,request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=LogForm()
    context={
        'form':form
    }
    return render(request,'login.html',context)


def log_out(request):
    logout(request)
    return redirect('home')