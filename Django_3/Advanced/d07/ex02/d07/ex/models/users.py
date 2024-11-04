from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password
        """
        if not username:
            raise ValueError("A username should be set")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None):
        """
        Creates and saved a superuser with the given username and password
        """
        user = self.create_user(
            username,
            password=password,
        )
        
        user.is_admin = True
        user.save(using=self.db)
        return user
    
class User(AbstractBaseUser):
    username = models.CharField(_("username"), max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    objects = CustomUserManager()
    
    class Meta:
        db_table = 'users'
    
    USERNAME_FIELD = "username"
    
    def __str__(self):
        return self.username