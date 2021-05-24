from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

# Credit:
# https://github.com/ckz8780/boutique_ado_v1/blob/master/products/widgets.py


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'toys/custom_widget_templates/custom_clearable_file_input.html'
