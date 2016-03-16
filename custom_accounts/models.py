from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("Please, enter a valid email address")

        user = self.model(
            email = self.normalize_email(email),
            is_active=True
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email,
        and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        # default='pralave.94@outlook.com',
        verbose_name='email address',
        unique=True,
        max_length=255,
        blank=False,
    )
    date_joined = models.DateTimeField(verbose_name='datetime',
                                       default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email
