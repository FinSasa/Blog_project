from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^contact/', include('blog.urls')),
    url(r'^news/', include('blog.urls')),

    #url(r'^redirectfb/', include('blog.urls')),
    #url(r'^redirectgg/', include('blog.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
