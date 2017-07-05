from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^blog/',ListView.as_view(
                            queryset=Post.objects.all().order_by("-date")[:25],
                            template_name="blog/news.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
                            model = Post,
                            template_name = "blog/post.html")),
    url(r'^redirectfb/', views.redirectfb, name='redirectfb'),
    url(r'^redirectgg/', views.redirectgg, name='redirectgg'),
    url(r'^search/', views.search, name='search'),
    #url(r'^comments/', include('django_comments_xtd.urls')),





    #url(r'^redirectfb/', views.redirectfb, name='redirectfb'),
    #url(r'^redirectgg/', views.redirectgg, name='redirectgg'),
]
