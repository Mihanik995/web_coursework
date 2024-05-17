from django.urls import path

from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, mailing_delete, \
    MailingMessageDetailView, MailingMessageCreateView, MailingMessageUpdateView, mailing_message_delete, client_delete, \
    ClientUpdateView, ClientCreateView, ClientDetailView, mailing_stop, mailing_finish, mailing_launch
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/new/', MailingCreateView.as_view(), name='add_mailing'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing/<int:pk>/stop/', mailing_stop, name='stop_mailing'),
    path('mailing/<int:pk>/finish/', mailing_finish, name='finish_mailing'),
    path('mailing/<int:pk>/launch/', mailing_launch, name='launch_mailing'),
    path('mailing/<int:pk>/delete/', mailing_delete, name='delete_mailing'),
    path('mailing_message/<int:pk>/', MailingMessageDetailView.as_view(), name='message_detail'),
    path('mailing_message/new/', MailingMessageCreateView.as_view(), name='add_message'),
    path('mailing_message/<int:pk>/update/', MailingMessageUpdateView.as_view(), name='update_message'),
    path('mailing_message/<int:pk>/delete/', mailing_message_delete, name='delete_message'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/new/', ClientCreateView.as_view(), name='add_client'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='update_client'),
    path('client/<int:pk>/delete/', client_delete, name='delete_client'),
]
