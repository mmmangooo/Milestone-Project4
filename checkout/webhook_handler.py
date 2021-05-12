from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

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
