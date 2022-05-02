from django import forms

# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]

# class ChooseProduct(forms.ModelForm):
#     product_choices = forms.ChoiceField(choices = FRUIT_CHOICES, label='a', required=True)

class ChoosePostTypeForm(forms.Form):
    choice = forms.ChoiceField(choices=([('', ''), ('Product', 'Product'), ('Service', 'Service')]), label='Create a new Product or Service')