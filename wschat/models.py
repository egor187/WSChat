from django.contrib.auth import get_user_model
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ChatRoom(TimeStampedModel):
    initiator = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='created_chat_rooms')
    members = models.ManyToManyField(get_user_model(), related_name='chat_rooms')
    private = models.BooleanField(default=False)


class Message(TimeStampedModel):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField(null=True, blank=True)
