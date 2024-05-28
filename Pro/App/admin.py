from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from .models import Profile, ChatMessage

class CustomAdminSite(AdminSite):
    site_header = 'Custom Admin Site'
    site_title = 'Custom Admin Site'
    index_template = 'admin/base_site.html'

custom_admin_site = CustomAdminSite(name='custom_admin')


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at')

# Register your models here
custom_admin_site.register(User)
custom_admin_site.register(Group)
custom_admin_site.register(Profile)
custom_admin_site.register(ChatMessage, ChatMessageAdmin)
