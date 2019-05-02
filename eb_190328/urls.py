from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^new/$', views.new, name="new"),
    url(r'^$', views.home, name="home"),
    url(r'^post/(?P<index>\d+)/$', views.post_detail, name="post_detail"), 
    url(r'^post/(?P<index>\d+)/edit/$', views.post_edit, name="post_edit"), 
]
