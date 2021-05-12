from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Order, OrderLineItem
from toys.models import Toy
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def send_confirmation_email(self, order):
        """ Sending confirmation email to user
        """
        client_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order,
            'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [client_email]
        )

    def handle_event(self, event):
        """
        Handling and unknown or unexpected webhook sent
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handling payment_intent.succeeded webhook
        """

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info 

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2) 

        # Cleaning data in shipping details 
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details_address[field] = None 

        # Updating profile information if save_info is checked

        profile = None
        username = intent.metadata.username 
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save() 

            order_exists = False
            attempt = 1
            while attempt <= 5:
                try:
                    order = Order.objects.get(
                        first_name__iexact=shipping.details.first_name,
                        last_name__iexact=shipping.details.last_name,
                        email__iexact=billing_details.email,
                        phone_number__iexact=shipping_details.phone,
                        country__iexact=shipping_details.address.country,
                        postcode__iexact=shipping_details.address.postal_code,
                        town_or_city__iexact=shipping_details.address.city,
                        street_address1__iexact=shipping_details.address.line1,
                        street_address2__iexact=shipping_details.address.line2,
                        county__iexact=shipping_details.address.state,
                        grand_total=grand_total,
                        original_bag=bag,
                        stripe_pid=pid,
                )

                except Order.DoesNotExist:
                    attempt += 1
                    time.sleep(1)

        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handling payment_intent_.payment_failed webhook 
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
