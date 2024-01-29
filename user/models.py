from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

#Custom manager for user profiles
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        #Create a new user
        if not email:
            raise ValueError('User must have an email address')

        # Normalize email address
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        # Save and Hash password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        # Create a superuser profile
        user = self.create_user(email, password, **extra_fields)

        # Set the user to be superuser
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

#Custom user model enables using email instead of username
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
