from django.contrib import admin
from .models import Chat, Group


class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'timestamps', 'group']
    ordering = ['-timestamps']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Chat, ChatAdmin)
admin.site.register(Group, GroupAdmin)
