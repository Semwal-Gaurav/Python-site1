from django.contrib import admin
from .models import UserRegisterForm, UserLogin

# Register your models here.

admin.site.register(UserRegisterForm)
admin.site.register(UserLogin)