from django import forms
from .models import UserProfile


class SignUpForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
      Add placeholders and remove labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postcode',
            'default_town_or_city': 'Town or City',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2',
            'default_county': 'County, state or region'
        }

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
