from django import forms
from django.db import models
from store.models import Bundle
from .models import Post, Customer, Vendor, User, Product, Service, Bundle, Wishlist



# class ChooseProduct(forms.Form):
class ChooseProduct(forms.Form):
    def __init__(self, choice_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'] = forms.ChoiceField(choices=choice_list, label='Select Product or Service')

    choice = forms.ChoiceField()


AXIS_CHOICES = [
    ('Cost', 'Cost')

]


# class ChooseRequirement(forms.Form):


# class addToWishlist(forms.Form):
#     choice = forms.CharField()


class ChoosePostTypeForm(forms.Form):
    choice = forms.ChoiceField(choices=([('', ''), ('Product', 'Product'), ('Service', 'Service')]), label='Create a new Product or Service')



class CreateBundle(forms.ModelForm):
    class Meta:
        model = Bundle
        fields = ['name', 'bundle_id', 'product_id', 'service_id', 'price', 'details']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['bundle_id'] = bundle_val

    name = models.CharField(("name"), max_length=255) 
    bundle_id = models.IntegerField(("bundle_id"), null=True, unique=False)
    product_id = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, blank=True, null=True, on_delete=models.CASCADE)
    price =  models.DecimalField(("price"), max_digits=10, decimal_places=2 , default=0)
    details = models.TextField()


# class AddToBundle(forms.ModelForm):