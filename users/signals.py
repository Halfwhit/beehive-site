from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from market.models import Transaction

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Transaction)
def authorised_transaction(sender, instance, **kwargs):
    if instance.authorised == True:
        sender = Profile.objects.get(user=instance.sender.id)
        recipient = Profile.objects.get(user=instance.recipient.id)
        if instance.direction == 'Sending':
            sender.balance -= instance.value
            recipient.balance += instance.value
        if instance.direction == 'Recieving':
            sender.balance += instance.value
            recipient.balance -= instance.value
        sender.save()
        recipient.save()