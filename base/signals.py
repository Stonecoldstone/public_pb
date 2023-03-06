from django.db.models.signals import pre_save
from django.contrib.auth.models import User


# Listener
def updateUser(sender, instance, **kwargs):
    """
    When click on save username becomes email
    https://www.udemy.com/course/django-with-react-an-ecommerce-website/learn/lecture/24599248#overview
    """
    print('Signal Triggered')


    user = instance

    if user.email != '':
        user.username = user.email



pre_save.connect(updateUser, sender=User)
