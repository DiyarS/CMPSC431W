from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import User as AuthUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """ A form for creating new users. Includes all the required fields, plus a repeated password. """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = AuthUser
        fields = ('email',)

    def clean_password2(self):
        #Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        #Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label="password",
                                         help_text="""Raw passwords are not stored, so there is no way to see this
                                         user's password, but you can change the password using <a href=\"password/\">
                                         this form</a>.""")

    class Meta(UserChangeForm.Meta):
        model = AuthUser
        fields = ('email', 'password', 'is_active', 'is_superuser', 'user_permissions')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class AuthUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_superuser')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(AuthUser, AuthUserAdmin)
=======


# Register your models here.


from .models import Items
admin.site.register(Items)

from .models import Category
admin.site.register(Category)

from .models import Fixed_Price
admin.site.register(Fixed_Price)

from .models import Auction
admin.site.register(Auction)

from .models import Belongs_to
admin.site.register(Belongs_to)

from .models import Registered_users
admin.site.register(Registered_users)

from .models import Sellers
admin.site.register(Sellers)

from .models import Companies
admin.site.register(Companies)

from .models import Individual_sellers
admin.site.register(Individual_sellers)

from .models import Individual_buyers
admin.site.register(Individual_buyers)

from .models import Address
admin.site.register(Address)

from .models import Delivers_to
admin.site.register(Delivers_to)

from .models import Has_address
admin.site.register(Has_address)

from .models import Credit_card
admin.site.register(Credit_card)

from .models import Has_credit_card
admin.site.register(Has_credit_card)

from .models import Bids
admin.site.register(Bids)

from .models import Buys
admin.site.register(Buys)














>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
