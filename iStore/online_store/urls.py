from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^register_new_user/$', views.register_new_user, name='register_new_user'),
]