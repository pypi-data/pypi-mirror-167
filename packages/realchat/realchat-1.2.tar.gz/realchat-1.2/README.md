realchat
==============================

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

Features

- One to one chat
- message encrypted before entering database
- Less hassle

realchat is a Django app to conduct web-based chat.

Detailed documentation is in the "docs" directory.

Quick start
------------

1. Add to your settings.py

     INSTALLED_APPS

          ```
               INSTALLED_APPS = [
                    'chat',
               ]
          ```

     To use the chat app, add it to your INSTALLED_APPS

     Auth_USER_MODEL

          ```
               AUTH_USER_MODEL = 'app.User' # it can be whatever user model you create
          ```

     The auth user model will communicate with the chat app and provide the user's name, email and auth status.

     LOGIN_URL

          ```
               LOGIN_URL = '/login/' # it can be whatever login url you create
          ```

     The login url provide url redirect from the chat view classes if the user is not logged in.

2. Include the chat URLconf in your project urls.py like this

          ```
               path('chat/', include('chat.urls')),
          ```

3. Templating \
     The chat app views return the following context variables:

MessageListView

context

     ```
     "inbox": # returns a dictionary of users you have chats with, 
               # and the latest message between you both
               # also including the time and unread message count
     ```

usage (django html)

     ```
          # use a for loop
          {% for key, item in inbox.items %}
               {{ key }} # to get the user you're chatting with 
               {{ item.message }} # to get the latest message between you two
               {{ item.date }} # the date the lastest message was sent
               {{ item.count }} # to get the unread messages count

               # to give access the inbox of the user, make each item template 
               # of the loop clickable and the url should be:
               {% url 'chat:inbox' key %}
          {% endfor %}
          # the url for messagelistview is:
          {% chat:message_list %}

     ```

InboxView

context

     ```
          "messages":     # returns all messages between you and the other user
          "other_person": # returns the user object of the person you're 
                         # chatting with
          "inbox":         # does the same as in the message list view, 
                         # it is passed to make sidepanel work like whatsapp web
          "you": #         # your user object is passed also 
     ```

usage (django html)

     ```
          # use a for loop
          {{ other_person.username }} # will get the username to display
          {% for message in messages%}
               # you can seperate user message and other user messages by
               # comparing the message sender and recipient objects
               # i.e
               {% if message.sender == other_person %}
               {{ message.message }}
               {{ message.date }}
               {% else %}
               # this will return messages that are not sent from the other_person
               {{ message.message }}
               {{ message.date }}
               {% endif %} 

          # finally, when sending messages to a user, create the following 
          # input tags in your from
               # hidden
               <input type="hidden" name="recipient" value="{{ other_person.pk }}">
               <input type="hidden" name="you" value="{{ you.pk }}">
          # get the message
          <input type=text name="message" placeholder="...">

          # the action of the form should be:
          {% url 'chat:inbox' other_person.username %}

          {% endfor %}

          # to use the inbox context,
          # extend the messaelist template
     ```

UserListView

context

     ```
          # usser list view has one context
          "users": # returns all users excluding the user logged in
     ```

usage

     ```
          # use a for loop and style your template however
     ```

4.Run `python manage.py migrate` to create the chat models.

5.Visit <http://127.0.0.1:8000/chat/> to participate in the to see a messages.

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
