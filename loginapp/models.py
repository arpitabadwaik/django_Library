from django.contrib.auth.models import User
from django.db import models

# Create your models here.

IS_DELETED = (
    (True, True),
    (False, False),
)

class SaveRegistrationData(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    e_mail = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField( max_length=100, blank=True, null=True)
    user_name = models.CharField(primary_key=True, max_length=100, blank=True,)
    password = models.CharField(max_length=100, blank=True, null=True)

class UserData(User):
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(choices=IS_DELETED, default=False)

    def __unicode__(self):
        return unicode(self.id)


