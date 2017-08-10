from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Helpr_User
from django.contrib.auth.models import User


"""
This wasn't working before the line: default_app_config = 'accounts.apps.AccountsConfig'
was added to __init__.py file..... figure out why

"""

@receiver(post_save, sender=User)
def connect_user(sender, instance=None, created=None, **kwargs):
    print('pre_save for {}'.format(sender.__name__))
    if created:
        print('First time creation')
        Helpr_User.objects.create(user=instance)
