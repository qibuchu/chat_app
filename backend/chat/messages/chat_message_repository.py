import os
from typing import List

import django
from channels.db import database_sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from chat.models import ChatMessage

#消息仓库
class ChatMessageRepository:
#获取聊天消息
    @database_sync_to_async
    def get_chat_messages(self, chat_id: str, order_by='timestamp') -> List[ChatMessage]:
        # Retrieve the chat history for `chat_id` from the database
        return list(ChatMessage.objects.filter(chat_id=chat_id).order_by(order_by))
#保存消息
    @database_sync_to_async
    def save_message(self, message: str, sender: str, chat_id: str):
        # Save the message to the database
        ChatMessage.objects.create(sender=sender, content=message, chat_id=chat_id)
