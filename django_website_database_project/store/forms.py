from django import forms

# class ChooseProduct(forms.Form):
class ChooseProduct(forms.Form, set):
    choice = forms.ChoiceField(choices=set, label='Select Product or Service')


AXIS_CHOICES = [
    ('Cost', 'Cost')

]

# class ChooseRequirement(forms.Form):
    

class ChoosePostTypeForm(forms.Form):
    choice = forms.ChoiceField(choices=([('', ''), ('Product', 'Product'), ('Service', 'Service')]), label='Create a new Product or Service')