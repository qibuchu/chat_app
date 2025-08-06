from django.contrib import admin

# Register your models here.

from .models import Chat, ChatMessage, Agent

admin.site.register(Chat)
admin.site.register(ChatMessage)
admin.site.register(Agent)
