from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts =[
    {
        'author':'Mallikarjun',
        'title':'1',
        'content':'First',
        'date':'March 25 2020' 

    },
    {
        'author':'Guru',
        'title':'2',
        'content':'Second',
        'date':'March 26 2020' 

    }


]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'word_freq_app/home.html',context)

def about(request):
    return render(request,'word_freq_app/about.html')