from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.contrib.contenttypes.models import ContentType

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)
    

class UserAccount(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password = models.CharField(max_length=255, null=True, blank=True)
    
    is_staff = models.BooleanField(default=False)  # Required for admin access
    is_superuser = models.BooleanField(default=False)  # Required for superuser access

    USERNAME_FIELD = 'username'  # Field used for authentication
    REQUIRED_FIELDS = ['email']  # Fields required for superuser creation

    objects = CustomUserManager()
    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        # If the password is not hashed, hash it before saving
        if self.password and not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)  # This hashes the password
        super(UserAccount, self).save(*args, **kwargs)

class UserAccountGroups(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        managed = True
        unique_together = (('user', 'group'),)


class UserAccountUserPermissions(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        managed = True
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        # db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE, null=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        unique_together = (('group', 'permission'),)
