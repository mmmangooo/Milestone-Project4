from django.shortcuts import render
from django.core.mail import send_mail


def contact(request):
    """
    View returning the contact page
    """
    if request.method == 'POST':
        input_name = request.POST['input_name']
        input_email = request.POST['input_email']
        input_message = request.POST['input_message']

        context = {
            'input_name': input_name,
            'input_email': input_email,
            'input_message': input_message,
        }

        return render(request, 'contact/contact.html', context)
    else:
        return render(request, 'contact/contact.html')
