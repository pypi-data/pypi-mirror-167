from django.db import models
from django_cryptography.fields import encrypt

from django.contrib.auth import get_user_model

UserProfile = get_user_model()

# Create your models here.
# ---------------------------------------------------------------------------- #
#                                 Message Model                                #
# ---------------------------------------------------------------------------- #


class Message(models.Model):
    sender          = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    recipient       = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='recipient')
    message         = encrypt(models.TextField())   # encrypt the message
    date            = models.DateTimeField(auto_now_add=True)
    sender_read     = models.BooleanField(default=False)
    recipient_read  = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'chat_messages'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('-date',)

    # function gets all messages between 'the' two users (requires your pk and the other user pk)
    def get_all_messages(id_1, id_2):
        messages = []
        # get messages between the two users, sort them by date(reverse) and add them to the list
        messages = [x for x in Message.objects.filter(sender_id=id_1, recipient_id=id_2)]  # get messages from recipient to sender and add them to the list

        messages += [x for x in  Message.objects.filter(sender_id=id_2, recipient_id=id_1)]  # get messages from recipient to sender to the list

        # because the function is called when viewing the chat, we'll return all messages as read
        for x in range(len(messages)):
            if messages[x].recipient == id_2: # check if the user logged in is the recipient
                messages[x].recipient_read = True
                messages[x].save()

        # sort the messages by date
        messages.sort(key=lambda x: x.date, reverse=False)

        return messages

    # function gets all messages between you and 'any' other user (requires your pk)
    def get_message_list(u):
        # get all the messages
        inbox = {}
        # update the inbox dictionary with the sender as the key
        [([(inbox.update({message.sender: inbox.get(message.sender, {
                                                    "username": message.sender.username,
                                                    "latest_message": message.message,
                                                    "send_date": message.date.strftime("%d/%m"),
                                                    "count": 0,
                                                    }
                                                )
                        }
                    ),
            )
            if message.sender != u
            # update the inbox dictionary with the recipient as the key
            else (inbox.update({message.recipient: inbox.get(message.recipient, {
                                                    "username": message.recipient.username,
                                                    "latest_message": message.message,
                                                    "send_date": message.date.strftime("%d/%m"),
                                                    "count": 0,
                                                    }
                                                )
                                }
                            ),
                )
            ],
            # update the count of unread messages
            {k: (inbox[k].update({"count": inbox[k].get("count", 0) + 1})
                    if message.recipient_read == False and message.sender == k
                    else inbox[k].update({"count": inbox[k].get("count", 0) + 0})
                    )
                for k in inbox.keys()
            }
        )
            for message in Message.objects.all()
            if message.sender == u or message.recipient == u
        ]

        return inbox
