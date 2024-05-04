from django.contrib import admin

from .models import Product, Shop, Order, User

admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Order)
admin.site.register(User)


