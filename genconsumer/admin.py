from django.contrib import admin
from .models import GenGroup, GenChat


class GenChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'createdAt']
    ordering = ['-createdAt']


class GenGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'group']


admin.site.register(GenChat, GenChatAdmin)
admin.site.register(GenGroup, GenGroupAdmin)
