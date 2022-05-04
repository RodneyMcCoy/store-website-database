from django import forms

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


class addToWishlist(forms.Form):
    choice = forms.CharField()


class ChoosePostTypeForm(forms.Form):
    choice = forms.ChoiceField(choices=([('', ''), ('Product', 'Product'), ('Service', 'Service')]), label='Create a new Product or Service')