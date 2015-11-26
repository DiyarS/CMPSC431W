from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Items, Category, Registered_users
from django.template import RequestContext, loader


def index(request):
    latest_items_list = Items.objects.order_by('item_id')[:100]
    template = loader.get_template('online_store/index.html')
    output = ', '.join([p.item_id for p in latest_items_list])
    context = RequestContext(request, { 'latest_items_list': latest_items_list,
    })
    return HttpResponse(template.render(context))


def shop(request):
	latest_question_list = Category.objects.order_by('name')[:5]
	template = loader.get_template('online_store/shop.html')
	context = RequestContext(request, {'latest_question_list': latest_question_list,
    }) 
	return HttpResponse(template.render(context))

def register_new_user(request):
    latest_question_list = Category.objects.order_by('name')[:5]
    template = loader.get_template('online_store/register_new_user.html')
    context = RequestContext(request, {'latest_question_list': latest_question_list,
    }) 
    return HttpResponse(template.render(context))