from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from toys.models import Toy
from profiles.models import UserProfile

import uuid


class Order(models.Model):
    """
    Defines the order in the db
    """
    order_number = models.CharField(
        max_length=32, null="False", editable="False")
    user_profile = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.CharField(max_length=254, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    country = CountryField(
        blank_label='Country', blank=False, null=False)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    town_or_city = models.CharField(max_length=40, blank=False, null=False)
    street_address1 = models.CharField(max_length=80, blank=False, null=False)
    street_address2 = models.CharField(max_length=80, blank=True, null=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generates a unique ordernumber
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updating the total order sum when a product is
        added to the order, and calulating delivery cost
        """
        self.order_total = self.lineitems.aggregate(Sum(
            'lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total + settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Setting order number if it's not set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Creates specification of ordered products and quantity
    """
    order = models.ForeignKey(
        Order, null=False, on_delete=models.CASCADE, related_name="lineitems")
    toy = models.ForeignKey(Toy, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Set lineitem total and update order total, overriding intital save
        """
        self.lineitem_total = self.toy.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.toy.sku} on order {self.order.order_number}'
