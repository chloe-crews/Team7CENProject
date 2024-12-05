from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Custom user manager for handling email-based authentication
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


# Custom user model with email, username, and password
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# Costume model for renting outfits
class Costume(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='costumes')
    title = models.CharField(max_length=255)  # Title of the costume
    description = models.TextField()  # Detailed description of the costume
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)  # Price for renting per day
    size = models.CharField(max_length=1)  # Costume size (S, M, L, etc.)
    category = models.CharField(max_length=30)  # Category (e.g., formal, costume, themed)
    available = models.BooleanField(default=True)  # Availability of the costume for rent
    date_listed = models.DateTimeField(auto_now_add=True)  # Automatically set the date the costume was listed

    def __str__(self):
        return self.title
