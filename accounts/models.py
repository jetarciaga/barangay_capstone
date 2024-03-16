from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    """Manager for user"""

    def create_user(self, email, password=None, **extra_fields):
        """Create a new user"""
        if not email:
            raise ValueError('User must provide an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a new super user with given details"""
        user = self.create(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    GENDER = {
        "M": "Male",
        "F": "Female",
        "N": "Prefer not to say"
    }

    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthday = models.DateField()
    mobile = PhoneNumberField(region='PHL')
    gender = models.CharField(max_length=1, choices=GENDER)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


