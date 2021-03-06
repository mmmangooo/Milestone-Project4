from django.db import models


class Category(models.Model):
    """ This model defines the Category
    model in the db and returns an instance of it"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name


class Toy(models.Model):
    """
    This model defines the Toy model
    in the db and returns an instance of it
    """

    name = models.CharField(max_length=254, blank=False, null=False)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=False, null=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    description = models.TextField(
        null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='toys', null=True, blank=True)
    campaign = models.BooleanField(default=False, null=True, blank=True)

    def get_price(self):
        """
        Check if toy is on campaign and if so calculate 20% discount
        on the price, and otherwise returning price
        """
        if self.campaign is True:
            price = self.price - (self.price*20/100)
            return price
        else:
            price = self.price
            return price

    def __str__(self):
        return self.name
