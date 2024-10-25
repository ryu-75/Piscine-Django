from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where username is the unique identifiers
    for authentication.
    """
    def create_user(self, username, password=None):
        """
        Create and save a user with the given username and password.
        """
        if not username:
            raise ValueError(_("The username must be set"))
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        """
        Create and save a SuperUser with the given username and password.
        """
        user = self.create_user(
            username,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.username
    
