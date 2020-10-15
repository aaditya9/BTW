from django.dispatch import receiver
from django.db.models.signals import ( post_save )
from btwapps.accounts.models.User import User
from btwapps.accounts.models.Profile import Profile



@receiver(post_save,sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )
