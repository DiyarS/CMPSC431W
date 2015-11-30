from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.
from models import Items, Category, Registered_users
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


def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    #user = auth.authenticate(username=username, password=password)
    found_user = None

    for user in Registered_users.objects.all():
        if (username == user.username) and (password == user.password):
            found_user = user
    
    if found_user is not None:
        #auth.login(request, user)
        return HttpResponseRedirect('/online_store/loggedin')
    else:
        return HttpResponseRedirect('/online_store/invalid_login')


def loggedin(request):
    return render_to_response('online_store/loggedin.html', 
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register_user(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('register.html', c)

def register_new_user(request):
    usernamE = request.POST.get('username', '')
    passworD = request.POST.get('password', '')
    emaiL = request.POST.get('email', '')
    phonE = request.POST.get('phone_number', '')

    new_user = Registered_users(username = usernamE, password = passworD, email = emaiL, phone_number = phonE)
    new_user.save()

    return HttpResponseRedirect('/online_store/invalid_login')
