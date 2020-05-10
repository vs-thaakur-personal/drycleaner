from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from auth.managers import user_manager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30, unique=True, blank=False)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_no = models.CharField(primary_key=True, max_length=10)
    alt_phone_no = models.CharField( max_length=10)
    password = models.CharField(max_length=30, blank=False)
    image = models.ImageField()
    area = models.CharField( max_length=200)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = ['first_name', 'address', 'phone_no', 'password']

    objects = user_manager.UserManager()

    def __str__(self):
        return f'first_name = {self.first_name}, last_name = {self.last_name},user_id = {self.user_id}' \
               f',phone_no = {self.phone_no},address = {self.address}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
