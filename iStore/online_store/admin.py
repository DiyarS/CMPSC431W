from django.contrib import admin


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














