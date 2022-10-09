from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import geocoder


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    # Overriding save method to get user location value
    def save(self, *args, **kwargs) -> None:
        # get goecode details
        user_location = geocoder.osm(self.address)
        lat = user_location.lat
        lng = user_location.lng

        # if the address is not found in Open Street Map API use arcgis
        if not lat or not lng:
            user_location = geocoder.arcgis(self.address)
            lat = user_location.lat
            lng = user_location.lng

        self.location = f'{lat} {lng}'

        # Override
        super(Profile, self).save(*args, **kwargs)

    def getlatlng(self) -> tuple:
        latlng = self.location.split()
        return float(latlng[0]), float(latlng[1])

    def get_user_profile(self):
        return f'{self.user.get_full_name()}\n{self.phone_number}\n{self.address}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
