from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone

class UserRegisterForm(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password_validator = [
        MinLengthValidator(8, message='Password must be at least 8 characters long.'),
        RegexValidator(
            regex='^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$',
            message='Password must contain at least one letter, one digit, and one special character.',
        )
    ]
    password = models.CharField(max_length=20, validators=password_validator)
    confirmpassword = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class UserLogin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    last_login = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username