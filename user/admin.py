from django.contrib import admin

from user.models import AbstractUser


@admin.register(AbstractUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', )
    autocomplete_fields = ('user', )
