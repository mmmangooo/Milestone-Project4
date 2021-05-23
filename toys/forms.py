from django import forms
from .widgets import CustomClearableFileInput
from .models import Toy

# Handling the forms image field credits:
# https://github.com/ckz8780/boutique_ado_v1/blob/master/products/forms.py


class ToyForm(forms.ModelForm):

    class Meta:
        model = Toy
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
