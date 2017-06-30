from django.shortcuts import render, redirect
from django.contrib import messages
from blog.forms import *
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from blog.models import Post
from django.conf import settings
from django.http.response import HttpResponseRedirect


def index(request):
    return render(request, 'blog/home.html')

def redirectfb(request):
    return redirect("https://www.facebook.com/tommaso.santi")

def redirectgg(request):
    return redirect("https://plus.google.com/u/0/113986302261523524607")


#def contact(request):
    #return render(request,'blog/basic.html',{'content':['If you would like to contact me, please email me.','salvatores1510@gmail.com']})

def news(request):
    return render(request, 'blog/news.html')

"""
def contact(request):
    return render(request, 'blog/contact.html')
"""
def search(request):
    if request.method == 'GET':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            print("validoooo")
            keyword = request.POST['keyword']
            articles = Post.objects.filter(title__icontains=keyword)
            if articles:
                print("qualcosa c'é " + str(articles.count()))
                return render(request, 'blog/news.html', {'object_list' : articles})
            else:
                return render(request, 'blog/articlenotfound.html')
        else:
            #messages.add_message(request, messages.INFO, str(form.errors))
            messages.warning(request, 'Invalid entry.')


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

"""
def email(request):
    if request_method == 'GET':

        addressform = forms.EmailAddressForm(request.GET)
        if addressform.addressValidation():
            subjectform = forms.EmailSubjectForm(request.GET)
            if subjectform.is_valid():
                textform = forms.EmailTextForm(request.GET)
                if textform.is_valid():
                    #email = request.GET['email'] #commented because the app uses the address located in settings.py
                    subject = request.GET['subject']
                    body = request.GET['body']
                    send_mail(subject, body, settings.EMAIL_HOST_USER, 'giulioartemio@gmail.com', fail_silently=False)
                    return render(request, 'blog/emailsent.html')
                else:
                    messages.warning(request, "Text's body is not valid.")
            else:
                messages.warning(request, "Email's subject is not valid.")
        else :
            messages.warning(request, "Email's address is not valid.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
"""

def contact(request):
    if request.method=='GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            address  = form.cleaned_data['address']
            subject  = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            try:
                send_mail(subject, body, address,  settings.EMAIL_HOST_USER)
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return render(request, 'blog/emailsent.html', {'form': form})
        else:
            form = ContactForm()

    return render(request, 'blog/contact.html', {'form':form})
