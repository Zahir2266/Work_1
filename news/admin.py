from django.contrib import admin
from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'content',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
