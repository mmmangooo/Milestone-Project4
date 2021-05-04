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
    image = models.ImageField
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    campaign_id = models.ForeignKey(
        'Campaign', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    """
    This model defines campaigns, related via foreign key
    to the toys that are on campaign
    """
    toy_id = models.ForeignKey(
        'Toy', null=True, blank=True,
        on_delete=models.SET_NULL)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.price)
