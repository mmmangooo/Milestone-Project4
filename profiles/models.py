from django.db import models
from django.contrib.auth.models import User
from db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model for storing and maintaining
    delivery information and order history for users
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email = models.Charfield(max_length=150, null=False, blank=False)
    default_phone_number = models.IntegerField(
        max_length=20, null=True, blank=True)
    default_country = models.CountryField(
        blank_label='Country', null=True, blank=True)
    default_postcode = models.IntegerField(
        max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_street_address_1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address_2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)

    def __Str__(self):
        return self.user.name

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """
        Create or update user profile
        """
        if created:
            UserProfile.objects.create(user=instance)
        # For existing user save the profile
        instance.userprofile.save()
