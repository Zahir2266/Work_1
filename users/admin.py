from django.contrib import admin
from users.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", 'group', ]
    search_fields = ["first_name", "last_name", "email", 'group', ]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
