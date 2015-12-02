from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shop/$', views.shop, name='shop'),
    #url(r'^register_new_user/$', views.register_new_user, name='register_new_user'),

    url(r'^login/$',  views.login),
    url(r'^login/auth/$',  views.auth_view),    
    url(r'^logout/$', views.logout),
    url(r'^loggedin/$', views.loggedin),
    url(r'^invalid_login/$', views.invalid_login),    
    url(r'^register/$', views.register),
    url(r'^register/register_new_user/$', views.register_new_user),
    url(r'^register_success/$', 'views.register_success'),
]