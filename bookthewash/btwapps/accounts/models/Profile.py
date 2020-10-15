from django.db import models

from btwapps.accounts.models.User import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.first_name


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )
        print(instance)
        print('Profile created !')


post_save.connect(create_profile, sender=User)