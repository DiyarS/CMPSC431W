from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django import template
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from models import Items, Category, User, RegistrationForm, AuthenticationForm, Fixed_Price, Auction, Belongs_to, Sellers, Companies, Individual_sellers, Individual_buyers, Address, Delivers_to, Has_address, Has_credit_card, Bids, Buys
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


register = template.Library()
@register.filter
def truncatechars(user_email, character):
    """
    Truncates a word after a given number of chars  
    Argument: Number of chars to truncate after
    """
    string = []
    if character in user_email:
        pos = user_email.find(character)
        for i in (0, pos-1):
            string.append(user_email[i])
    return ''.join(string)




def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render_to_response('register.html', {
        'form': form,
    }, context_instance=RequestContext(request))


def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login.html', c)



def auth_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return HttpResponseRedirect('/online_store/loggedin')
            else:
                return HttpResponseRedirect('/online_store/invalid_login')
    else:
        form = AuthenticationForm()
    return render_to_response('login.html', {
        'form': form,
    }, context_instance=RequestContext(request))


def loggedin(request):
    user = request.user.email
    string = []
    character = '@'
    if character in user:
        pos = user.find(character)
        for i in (0, pos-1):
            string.append(user[i])
    user = ''.join(string)
    return render_to_response('online_store/loggedin.html', 
                              {'user_email': user})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
#def logout(request):
 #   """
  #  Log out view
   # """
    #django_logout(request)
    #return redirect('logout.html')

def register_user(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('register.html', c)



def retrieve_id_of_registered_user(user_email):
    for user in User.objects.all():
        if user.email == str(user_email) + '@gmail.com':
            return int(user.id)

    return None


def register_new_user(request):
    if request.method == 'POST':
        #usernamE = request.POST.get('username', '')
        #password = request.POST.get('password', '')
        #emaiL = request.POST.get('email', '')
        #phonE = request.POST.get('phone_number', '')

        form = RegistrationForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/online_store/register_success')
        else:
            return HttpResponseRedirect('online_store/loggedin.html')

    else:
        form = RegistrationForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('invalid_login.html', args)





def add_item_for_sell(request, user_email):
    c = {}
    c.update(csrf(request))
    return render_to_response('add_item_for_sell.html', {'user_email': user_email})


@csrf_exempt
def submit_item_to_sell(request, user_email):
    """
    View for filling out information about an item to sell
    """
    if request.method == 'POST':
        new_item = Items()

        max_id_value = 0
        for existing_item in Items.objects.all():
            last_id = existing_item.item_id
            if int(last_id) > max_id_value:
                max_id_value = int(last_id)

        new_id = str(max_id_value+1)
        new_item.item_id = new_id
        new_item.item_name = request.POST.get('item_name')
        new_item.description = request.POST.get('description')
        new_item.location = request.POST.get('location')
        new_item.save()



        new_user = True
        #search for users
        for user in Sellers.objects.all():
            if user.seller_id == request.POST.get('user_email'):
                user.item_id_id = new_item.item_id
                new_user = False
                user.save()

        if new_user == True:
            new_seller = Sellers()
            new_seller.username_id = retrieve_id_of_registered_user(request.POST.get('user_email'))
            idd = new_seller.username_id

            if request.POST.get('user_email') == None:
                new_seller.seller_id = 'empty'
            else:
                new_seller.seller_id = request.POST.get('user_email')
            new_seller.item_id_id = new_item.item_id
            use = request.GET.get('user_email')
            new_seller.save()



        price_entry_for_new_item = Fixed_Price()
        price_entry_for_new_item.item_id = new_item
        price_entry_for_new_item.price = request.POST.get('price')
        price_entry_for_new_item.save()

        item_belongs_to = Belongs_to()
        item_belongs_to.item_id = new_item
        item_belongs_to.category = 'Books'
        item_belongs_to.save()


    #return render_to_response('add_item_for_sell.html')
    return HttpResponseRedirect('/online_store/submitted_item_to_sell', {'user_email': user_email} )



def search_description(query):
    items_to_output = []
    for item in Items.objects.all():
        for string in item.description.split():
            if string == query:
                items_to_output.append(item)
                break 

    return items_to_output


def search(request):
    """
    View for filling out information about an item to sell
    """
    if request.method == 'GET':
        item_name_to_search = request.GET.get('query')
        items_to_output = search_description(item_name_to_search)



    #return render_to_response('add_item_for_sell.html')
    return render_to_response('search.html', {'query': request.GET.get('query'), 'items': items_to_output})











def submitted_item_to_sell(request):
    return render_to_response('submitted_item_to_sell.html')

def personal_account(request, user_email):
    #return HttpResponse("You're voting on question %s." % user_email)
    return render_to_response('personal_account.html', {'user_email': user_email})

