from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from utils.date_time_models import TimeFieldModel

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_fields) 
        user.set_password(password) 
        user.save(using=self._db) 
        
        return user

    def get_by_natural_key(self, email):
        # Se utiliza el email para encontrar el usuario
        return self.get(email=email)
    
    def create_superuser(self, email, password=None, **extra_fields):
        # Asegúrate de que el usuario sea un superusuario
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin, TimeFieldModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    class Meta():
        db_table = 'users'

    def __str__(self):
        return self.email








