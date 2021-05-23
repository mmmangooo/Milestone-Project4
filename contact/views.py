# Code credits for send email functionality
# https://docs.djangoproject.com/en/3.2/topics/email/
# https://docs.djangoproject.com/en/3.2/topics/forms/
# https://www.youtube.com/watch?v=w4ilq6Zk-08&list=PLXcnmXd-db_hO1v3SLAzVcNieoS_Tcn-6&index=6

from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """
    View returning the contact page and handling the user sending emails
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            input_email = contact_form.cleaned_data['input_email']
            input_name = contact_form.cleaned_data['input_name']
            input_message = contact_form.cleaned_data['input_message']

            try:
                # Sending an email
                send_mail(
                    f'Message from {input_name}',  # Subject
                    input_message,  # Message
                    input_email,  # From Email
                    [settings.DEFAULT_FROM_EMAIL],  # To email
                    fail_silently=False,  # Raise SMTPException if send fails
                )

                # Success message to user if send email succeeds,
                # and redirecting user back to contact page
                messages.success(
                    request,
                    f'Thank you {input_name}, your email has been sent to us!')
                return HttpResponseRedirect('/contact/')

            # Preventing malicious injections of to or from values
            # in the email header
            except BadHeaderError:
                return HttpResponse('Invalid header found')

        # Handling email send failings with message to user and
        # redirect user back to contact page
        else:
            messages.error(request, 'Your email could not be sent.\
                    Please check if the contact form is valid')
            return redirect(reverse, 'contact')

    else:
        # Inserting a logged in user's saved email into the contact form
        if request.user.is_authenticated:
            input_email = request.user.email
            contact_form = ContactForm(
                initial={'input_email': request.user.email}
            )
        else:
            contact_form = ContactForm()

    context = {
            'contact_form': contact_form,
            }

    return render(request, 'contact/contact.html', context)
