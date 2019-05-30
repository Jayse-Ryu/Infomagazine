from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django_enumfield import enum

from organization.models import Organization


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        db_table = 'user'


class AccessRole(enum.Enum):
    OWNER = 0
    MARKETER = 1
    CLIENT = 2
    GUEST = 3


class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='info')
    access_role = enum.EnumField(AccessRole, default=AccessRole.GUEST)
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL)
    phone_num = models.CharField(max_length=11)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_info'
