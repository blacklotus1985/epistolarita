from django.db.models.signals import post_save
from django.conf import settings
from django.db import models

User_Model = settings.AUTH_USER_MODEL


class User(models.Model):
    """
    User model which inherites the AUTH USER MODEL class
    Class for creating new user
    """
    user = models.OneToOneField(User_Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


def user_data_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = User.objects.create(user=instance)


post_save.connect(user_data_receiver, sender=User_Model)
