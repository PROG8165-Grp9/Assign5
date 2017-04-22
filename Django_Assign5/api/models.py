from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your models here.


class Transactions(models.Model):

    Trans_Desc = models.TextField()
    Owner = models.ForeignKey(
        'auth.User',
        related_name='transactions',
        on_delete=models.CASCADE)
    Trans_Date = models.DateTimeField()
    Trans_Type = models.CharField(max_length=50)
    Trans_Loc = models.CharField(max_length=150)
    Trans_Amnt = models.DecimalField(decimal_places=2, max_digits=150, default=0)
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Category(models.Model):
    Cate_Type = models.CharField(max_length=50)
    Cate_Desc = models.TextField()

