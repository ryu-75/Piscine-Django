from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Permission
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.db import models

class CustomUserManager(BaseUserManager):
    def attr_permission(self, username):
        try:
            users = get_object_or_404(Users, pk=username)
            delete_tip_permission = Permission.objects.get(
                codename='auth_delete_tip',
                name='can delete tip',
            )
            add_downvote_permission = Permission.objects.get(
                codename='can_add_downvote',
                name='can add downvote',
            )
            users.user_permissions.add(delete_tip_permission, add_downvote_permission)
            users.has_perm('ex.can_add_downvote')
            users.has_perm('ex.can_delete_tip')
            users = get_object_or_404(Users, pk=username)
        except Permission.DoesNotExist:
            print(f"auth_delete_tip permission is not exist.")
    
    """
    Custom user model manager where username is the unique identifiers
    for authentication.
    """
    def create_user(self, username, password=None, reputation=0):
        """
        Create and save a user with the given username and password.
        """
        if not username:
            raise ValueError(_("The username must be set"))
        user = self.model(username=username, reputation=reputation)
        user.set_password(password)
        user.save(using=self._db)
        self.attr_permission(user)
        return user
    
    def create_superuser(self, username, password, reputation):
        """
        Create and save a SuperUser with the given username and password.
        """
        user = self.create_user(
            username,
            password=password,
            reputation=reputation
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=200, unique=True)
    reputation = models.IntegerField(_("reputation"), default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.username
