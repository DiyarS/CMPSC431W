import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django import forms
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.utils.translation import gettext as _

# Create your models here
class Items(models.Model):
	class Meta:
		verbose_name_plural = "Items"
	item_id = models.CharField(max_length=30, unique=True, primary_key=True )
  	item_name = models.CharField(max_length=100, null = True)
    	description = models.CharField(max_length=500)
	location = models.CharField(max_length=60)
	rating = models.FloatField(null=True)

class  Category(models.Model):
	class Meta:
		verbose_name_plural = "Categories"
    	name = models.CharField(max_length=60, unique=True, primary_key=True)
    	subcategory = models.ForeignKey('self', null=True)
    	parent_cat = models.ForeignKey('self', related_name = 'parent_category', null=True)
    	report = models.TextField(max_length=1000)

    	def __iter__(self):
    		return [self.name, self.subcat, self.parent_cat, self.report]


class  Fixed_Price(models.Model):
	class Meta:
		verbose_name_plural = "Fixed_Prices"
    	item_id = models.ForeignKey(Items, unique=True, primary_key=True)
    	price = models.FloatField()


class  Auction(models.Model):
	class Meta:
		verbose_name_plural = "Auctions"
    	item_id = models.ForeignKey(Items, unique=True, primary_key=True)
    	BID = models.FloatField() 
    	reserve_price = models.FloatField()
    	expiration_time = models.DateTimeField()


class  Belongs_to(models.Model):
	class Meta:
		verbose_name_plural = "Belongs_to"
    	category = models.CharField(max_length=30)
    	item_id = models.ForeignKey(Items , primary_key=True) 
    	#subcategory = models.ForeignKey(Category, related_name = 'subcategory')
    	#parent_category = models.ForeignKey(Category, related_name = 'parent_category')

class UserManager(BaseUserManager):
    

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :param bool is_staff: whether user staff or not
        :param bool is_superuser: whether user admin or not
        :return custom_user.models.EmailUser user: user
        :raise ValueError: email is not set
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        user = self.model(email=email, is_staff=is_staff, is_active=is_active,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: regular user
        """
        is_staff = extra_fields.pop("is_staff", False)
        return self._create_user(email, password, is_staff, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: admin user
        """
        return self._create_user(email, password, True, True,
                                 **extra_fields)


    


class  User(AbstractBaseUser, PermissionsMixin):

    """
    Custom user class.
    """

    email = models.EmailField(_('email address'), max_length=255,
                              unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    phone_number = models.CharField(max_length=30)
    review = models.CharField(max_length=200, default='null')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    	
    def __unicode__(self):
    	return unicode(self.email)



class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    email = forms.EmailField(widget=forms.widgets.TextInput,label="Email")
    password1 = forms.CharField(widget=forms.widgets.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.widgets.PasswordInput,
                                label="Password (again)")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class AuthenticationForm(forms.Form):
    """
    Login form
    """
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['email', 'password']

class  Sellers(models.Model):
	class Meta:
		verbose_name_plural = "Sellers"
    	username = models.ForeignKey(User, primary_key=True, unique = True, default = "user")
    	seller_id = models.CharField(max_length=30, unique=True)
        item_id = models.ForeignKey(Items, null = True)


class  Companies(models.Model):
	class Meta:
		verbose_name_plural = "Companies"
    	username = models.ForeignKey(Sellers, to_field='username_id', default='null', primary_key=True)
    	seller_id = models.ForeignKey(Sellers, to_field='seller_id', related_name='seller_id_id', default='-1')
    	name = models.CharField(max_length=30)
    	point_of_contact = models.CharField(max_length=50)
    	revenue = models.FloatField()


class  Individual_sellers(models.Model):
	class Meta:
		verbose_name_plural = "Individual_sellers"
    	username = models.ForeignKey(Sellers, to_field='username_id', default='null', primary_key=True)
    	seller_id = models.ForeignKey(Sellers, to_field='seller_id', related_name = 'individual_seller_id')
    	dob = models.DateField('date_of_birth')
    	gender = models.CharField(max_length=10)
    	annual_income = models.FloatField()

class  Individual_buyers(models.Model):
	class Meta:
		verbose_name_plural = "Individual_buyers"
    	username = models.ForeignKey(User, primary_key=True)
    	buyer_id = models.CharField(max_length=30, unique=True)
    	dob = models.DateField('date_of_birth')
    	gender = models.CharField(max_length=10)
    	annual_income = models.FloatField()

class Address(models.Model):
	class Meta:
		verbose_name_plural = "Addresses"
	street = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 30)
	index = models.CharField(max_length = 20)
	primary = models.IntegerField(unique=True)

class  Delivers_to(models.Model):
	class Meta:
		verbose_name_plural = "Delivers_to"
    	seller_id = models.ForeignKey(Sellers, to_field='seller_id', default='null')
    	buyer_id = models.ForeignKey(Individual_buyers, to_field='buyer_id', default='null')
    	address = models.ForeignKey(Address)
    	payment_confirmation = models.BooleanField()


class Has_address(models.Model):
	class Meta:
		verbose_name_plural = "Has_addresses"
	username = models.ForeignKey(User)
	primary = models.ForeignKey(Address, to_field='primary')

class Credit_card(models.Model):
	class Meta:
		verbose_name_plural = "Credit_cards"
	card_number = models.CharField(max_length=20, unique=True)
	name_on_card = models.CharField(max_length=40)
	expiration_date = models.DateField('expiration_date')
	code = models.CharField(max_length=4)
	primary = models.IntegerField()

class Has_credit_card(models.Model):
	class Meta:
		verbose_name_plural = "Has_credit_cards"
	username = models.ForeignKey(User)
	primary = models.ForeignKey(Credit_card)


class Bids(models.Model):
	class Meta:
		verbose_name_plural = "Bids"
	item_id = models.ForeignKey(Auction)
	BID = models.FloatField()
	username = models.ForeignKey(User)

class Buys(models.Model):
	class Meta:
		verbose_name_plural = "Buys"
	item_id = models.ForeignKey(Fixed_Price)
	username = models.ForeignKey(User)

