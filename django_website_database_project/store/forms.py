from django import forms
from django.db import models
from .models import Product, Service


class ChooseProduct(forms.Form):
    p_models = Product.objects.all()
    p_list = set()

    for product in p_models:
        p_type = product.product_type    
        p_list.add( (str(p_type), str(p_type)) ) 
    
    p_models = Service.objects.all()

    for service in p_models:
        p_type = service.service_type
        p_list.add( (str(p_type), str(p_type)) ) 

    if(len(p_list) == 0):
        p_list.add( ("no products in database", "no products in database") )

    choice = forms.ChoiceField(choices=p_list, label='Select Product or Service')


AXIS_CHOICES = [
    ('Cost', 'Cost')

]

# class ChooseRequirement(forms.Form):
    

class ChoosePostTypeForm(forms.Form):
    choice = forms.ChoiceField(choices=([('', ''), ('Product', 'Product'), ('Service', 'Service')]), label='Create a new Product or Service')