from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from django.contrib.auth.hashers import make_password
    
class UserManager(BaseUserManager):
    def _create_user(self, username,  password, is_active, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            is_active = is_active,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username,  password=None, **extra_fields):
        return self._create_user(self, username, password, True, False, False, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        return self._create_user(username, password, True, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('usuario',max_length = 255, unique = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    #def natural_key(self):        return(self.username)
    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['email','name','last_name','firm', 'direc', 'office', 'telephone']

    #contructor
    def __str__(self):
       return f'{self.username}'
