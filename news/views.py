from django.shortcuts import render,get_object_or_404
from .models import News , Category



def homepage(request):
    news=News.objects.all()
    categories=Category.objects.all()
    return render(request,'home.html',{'news':news,'categories':categories})


def detail(request,id):
    news=get_object_or_404(News,id=id)
    return render(request,'detail.html',{'abc':news})

def category_funk(request,id):
    categories=Category.objects.all()
    news=News.objects.filter(category_id=id)
    return render(request,'category.html',{'news':news,'categories':categories})





