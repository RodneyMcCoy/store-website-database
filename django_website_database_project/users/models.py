from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='icon1.png', upload_to='')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

""""
#Work in progress for different users.
#This is a condensed version, but still creates errors
#hence why it is commented

class User(AbstractUser):
    class Types(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        VENDOR =  "VENDOR", "Vendor"

    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=Types.CUSTOMER)

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

class Customer(User):
    class Meta:
        proxy = True
        
class Vendor(User):
    class Meta:
        proxy = True
"""