from django.contrib import admin
from .models import User, Post, Customer, Vendor, Bundle, Product, Service, Wishlist

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Bundle)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Wishlist)