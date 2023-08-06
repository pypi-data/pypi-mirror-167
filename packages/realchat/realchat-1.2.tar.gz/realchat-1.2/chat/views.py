from django.conf import settings
from .models import Message
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import get_user_model

UserProfile = get_user_model()

login_url = settings.LOGIN_URL

# Create your views here.

# ---------------------------------------------------------------------------- #
#                               Class based Views                              #
# ---------------------------------------------------------------------------- #

# ----------------------- Inbox/messages/users list ----------------------- #
class MessagesListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'chat/messages_list.html'
    login_url = login_url

    # context data for latest message to display
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = UserProfile.objects.get(pk=self.request.user.pk)  # get user
        inbox = Message.get_message_list(user) # get latest message and unread count

        context['inbox'] = inbox
        return context


# --------------------------------- Chat view -------------------------------- #
class InboxView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'chat/inbox.html'
    login_url =  login_url
    queryset = UserProfile.objects.all()

    # to send a message (pass the username instead of the primary key to the post function)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    # overide detailview default request pk or slug to get username instead
    def get_object(self):
        UserName= self.kwargs.get("username")
        return get_object_or_404(UserProfile, username=UserName)

    # context data for the chat view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = UserProfile.objects.get(pk=self.request.user.pk)  # get user
        other_user = UserProfile.objects.get(username=self.kwargs.get("username"))  # get the other user's primary key
        inbox = Message.get_message_list(user) # get latest message and unread count

        sender = other_user  # the sender of the message will be the recipient of the most recent message after it's sent
        recipient = user # the recipient of the message will be the sender of the most recent message after it's sent

        context['messages'] = Message.get_all_messages(sender, recipient)  # get all the messages between the sender(you) and the recipient (the other user)
        context['other_person'] = other_user  # get the other person you are chatting with from the username provided
        context['inbox'] = inbox
        context['you'] = user

        return context

    # send a message
    def post(self, request, *args, **kwargs):
        sender = UserProfile.objects.get(pk=request.POST.get('you'))
        recipient = UserProfile.objects.get(pk=request.POST.get('recipient'))  # this will be passed from the templates
        message = request.POST.get('message')  # get the message from the form

        if request.method == 'POST':
            if message:
                # sender_read will be set to true everythime a message is sent
                Message.objects.create(sender=sender, recipient=recipient, message=message, sender_read=True)
        return redirect('chat:inbox', username=recipient.username)  # redirect to the inbox of the recipient


# -------------------------------- Users list (find other users on the platform) -------------------------------- #
class UserListsView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'chat/users_list.html'
    context_object_name = 'users'
    login_url = login_url

    # context data for the users list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = UserProfile.objects.get(pk=self.request.user.pk)  # get your primary key
        context['users'] = UserProfile.objects.exclude(pk=user.pk)  # get all the users except you
        return context