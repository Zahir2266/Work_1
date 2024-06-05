from django.contrib import admin
from users.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", 'role', ]
    search_fields = ["first_name", "last_name", "email", 'role', ]
