from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

# class UserProfileManager(BaseUserManager, PermissionsMixin):
#     # Managers for the user profiles
#     def create_user(self, email, name, password=None):
#         #Create a new user profile
#         if not email:
#             raise ValueError("User must have an email Address")

#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)

#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, name, password):
#         user = self.create_user(email, name, password)

#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)


# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     # Database model for users in the system
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=40)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserProfileManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         #Get full name of User
#         return self.name

#     def get_short_name(self):
#         #Get short name of the user
#         return self.name

#     def __str__(self):
#         return self.email