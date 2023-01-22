from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def created_user(sender, instance, created, **kwargs):
    if created:
        new_pro = Profile.objects.create(user=instance)
        new_pro.save()
