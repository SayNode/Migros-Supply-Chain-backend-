from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'{instance.username}/{filename}'



class User(AbstractUser):
    # Field used for login
    USERNAME_FIELD = 'email'

    # Additional fields required when using createsuperuser
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        ("username"),
        max_length=150,
        unique=True,
        validators=[username_validator],
        blank=True,
        null=True,
    )

    phone = models.CharField(max_length=20, blank=True, null=True)

    wallet_address = models.CharField(max_length=255, blank=True, null=True)

    role = models.CharField(max_length=255, blank=True, null=True)

    balance = models.IntegerField(blank=True, null=True, default=0)


    # Social Profile
    avatar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)


    about_me = models.CharField(
        verbose_name='user description',
        max_length=1000,
        blank=True
    )


    def __str__(self):
        return f'User {self.pk}: {self.email}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.username
