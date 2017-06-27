from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),


    # url(r'^$', ListView.as_view(
            #               queryset=Post.objects.all().order_by("-date")[:25],
            #               template_name="blog/news.html")),


    url(r'^contact/', views.contact, name='contact'),

    url(r'^blog/',ListView.as_view(
                            queryset=Post.objects.all().order_by("-date")[:25],
                            template_name="blog/news.html")),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(
                            model = Post,
                            template_name = "blog/post.html")),


]
