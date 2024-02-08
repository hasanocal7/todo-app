from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(instance.username, '___Created: ', created)
    if created:
        UserProfile.objects.create(user=instance)