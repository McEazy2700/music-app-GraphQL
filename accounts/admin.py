from django.contrib import admin
from eazy_user.models import EmailUser
# Register your models here.

@admin.register(EmailUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_joined']