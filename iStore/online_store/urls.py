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
    #url(r'^register_success/$', views.register_success),
    url(r'^add_item_for_sell/(?P<user_email>\w+)/$', views.add_item_for_sell),
    url(r'^add_item_for_sell/(?P<user_email>\w+)/submit_item_to_sell/$', views.submit_item_to_sell),
    url(r'^submitted_item_to_sell/$', views.submitted_item_to_sell),
    url(r'^personal_account/(?P<user_email>\w+)/$', views.personal_account),
    url(r'^search/$', views.search),
    #url(r'^personal_account/my_products$', views.my_products),
    #url(r'^personal_account/my_orders$', views.my_orders),
]