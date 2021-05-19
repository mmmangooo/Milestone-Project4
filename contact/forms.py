# Credit: https://docs.djangoproject.com/en/3.2/topics/forms/

from django import forms


class ContactForm(forms.Form):
    """
    Contact form
    """
    input_email = forms.EmailField()
    input_name = forms.CharField(max_length=100)
    input_message = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ['input_email', 'input_name', 'input_message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setting placeholders on fields
        placeholders = {
            'input_email': 'Email',
            'input_name':  'Name',
            'input_message': 'Message'
        }

        self.fields['input_email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
