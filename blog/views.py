from django.shortcuts import render

def index(request):
    return render(request, 'blog/home.html')

def contact(request):
    return render(request,'blog/basic.html',{'content':['If you would like to contact me, please email me.','salvatores1510@gmail.com']})

def news(request):
    return render(request, 'blog/news.html')
