from django import forms
from .widgets import CustomClearableFileInput
from .models import Toy


class ToyForm(forms.ModelForm):

    class Meta:
        model = Toy
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
