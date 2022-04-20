from cgi import print_exception
from curses import BUTTON1_DOUBLE_CLICKED
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# Each class is its own table in the database
# Each class attribute is a field in the database

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Bundle(models.Model):
    vendor_id = models.IntegerField(("vendor_id"))
    price =  models.DecimalField(("price"), max_digits = 6, decimal_places= 2 )

class Customer(models.Model):
    name = models.CharField(("name"), max_length=255)
    background = models.CharField(("background"), max_length = 300)

class Product(models.Model):
    product_type = models.CharField(("product_type"), max_length=255)
    vendor_id = models.IntegerField(("vendor_id"))
    bundle_id = models.IntegerField(("bundle_id"))
    product_name = models.CharField(("product_name"), max_length=255)
    price =  models.DecimalField(("price"), max_digits = 6, decimal_places= 2 )
    binding_contract = models.CharField(("binding_contract"), max_length=255)

class Service(models.Model):
    service_type = models.CharField(("service_type"), max_length=255)
    vendor_id = models.IntegerField(("vendor_id"))
    bundle_id = models.IntegerField(("bundle_id"))
    service_name = models.CharField(("service_name"), max_length=255)
    price =  models.DecimalField(("price"), max_digits = 6, decimal_places= 2 )
    binding_contract = models.CharField(("binding_contract"), max_length=255)

class Vendor(models.Model):
    name = models.CharField(("name"), max_length=255)

class Wishlist(models.Model):
    customer_id = models.IntegerField(("customer_id"))
    service_id = models.IntegerField(("service_id"))
    product_id = models.IntegerField(("product_id"))