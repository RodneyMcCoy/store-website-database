import imp
from django.db.models.signals import post_save
#from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from store.models import User, Customer, Vendor

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created and instance.is_customer:
        Customer.objects.create(user=instance, name=instance.username, background='A background')


@receiver(post_save, sender=User)
def create_vendor(sender, instance, created, **kwargs):
    if created and instance.is_vendor:
        Vendor.objects.create(user=instance, name=instance.username)