from django import forms
from .widgets import CustomClearableFileInput
from .models import Toy, Category


class ToyForm(forms.ModelForm):

    class Meta:
        model = Toy
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
