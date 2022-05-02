from cgi import print_exception
from typing import Tuple
#from curses import BUTTON1_DOUBLE_CLICKED
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
# Each class is its own table in the database
# Each class attribute is a field in the database


# This model class contains extra information related to the default User model class
class User(AbstractUser):
    """
    Adds additional information onto the default User class
    In particular, adds extra fields to determine if the user is a vendor or customer
    """
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


# This model class contains information related to an entry of an item visible to customers
class Post(models.Model):
    """
    Contains information regarding a product or service post
    This includes all necessary content to show a customer (or vendor) all the associated relevant information
    Information includes title of post, content, date posted, and author (vendor owner)
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# This model class contains information related to the customer, which is an 'overwrite' of the base User class
class Customer(models.Model):
    """
    Contains information related to a customer. Note that a customer is a modified, one-to-one relation of the base User class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(("name"), max_length=255)
    background = models.CharField(("background"), max_length = 300)

    USERNAME_FIELD = 'user'

    def __str__(self):
        return f'{self.user.username}\'s customer details'


# This model class contains information related to the vendor, which is an 'overrwrite' of the base User class
class Vendor(models.Model):
    """
    Contains information related to a vendor. Note that a vendor is a modified, one-to-one relation of the base User class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(("name"), max_length=255)

    USERNAME_FIELD = 'user'

    def __str__(self):
        return f'{self.user.username}\'s vendor details'


# This model class contains information related to bundle specifics for products and/or services
class Bundle(models.Model):
    """
    Contains information relevant to a product and/or service bundle of a specific vendor
    """
    #bundle_id = models.AutoField(primary_key=True)
    #vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_id = models.IntegerField(("vendor_id"))
    price =  models.DecimalField(("price"), max_digits=10, decimal_places=2 , default=0)

    def __str__(self):
        return f'Bundle {self.vendor_id}'


# This model class contains information related to a specific product that will be visible on the website to users
class Product(models.Model):
    """
    Contains information related to a product posted by a vendor that is avaiable for 'purchase' on the website
    This includes all necessary content on the product to give the customer a complete understanding of what the product entails
    """
    #product_id = models.AutoField(primary_key=True)
    product_type = models.CharField(("product_type"), max_length=255)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    #bundle_id = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    #vendor_id = models.IntegerField(("vendor_id"))
    bundle_id = models.IntegerField(("bundle_id"))
    product_name = models.CharField(("product_name"), max_length=255)   # Like title for Post
    price =  models.DecimalField(("price"), max_digits=10, decimal_places=2, default=0)
    binding_contract = models.CharField(("binding_contract"), max_length=255)
    details = models.TextField()    # Like content for Post

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Like author for Post

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('store-home')


# This model class contains information related to a specific service that will be visible on the website to users
class Service(models.Model):
    """
    Contains information related to a service posted by a vendor that is available for 'purchase' on the website
    This includes all necessary content on the service to give the customer a complete understanding of what the service entails
    """
    #service_id = models.AutoField(primary_key=True)
    service_type = models.CharField(("service_type"), max_length=255)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    #bundle_id = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    #vendor_id = models.IntegerField(("vendor_id"))
    bundle_id = models.IntegerField(("bundle_id"))
    service_name = models.CharField(("service_name"), max_length=255)   # Like title for Post
    price =  models.DecimalField(("price"), max_digits=10, decimal_places=2, default=0)
    binding_contract = models.CharField(("binding_contract"), max_length=255)
    details = models.TextField()    # Like content for Post

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Like author for Post

    def __str__(self):
        return self.service_name

    def get_absolute_url(self):
        return reverse('store-home')


# This model class contains information related to the wishlist of a customer, which contains any products or services they have wishlisted
class Wishlist(models.Model):
    """
    Contains information relating a customer with the items they desire to obtain.
    This allows the associated customer to quickly view all saved products and services that they previously added to their personal wishlist
    """
    #wishlist_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    #customer_id = models.IntegerField(("customer_id"))
    #service_id = models.IntegerField(("service_id"))
    #product_id = models.IntegerField(("product_id"))