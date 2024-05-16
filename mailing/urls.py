from django.urls import path

from mailing.views import MailingListView, MailingDetailView, MailingCreateView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/new/', MailingCreateView.as_view(), name='add_mailing'),
    # path('mailing/<int:pk>/update', MailingUpdateView.as_view(), name='update_mailing'),
    # path('mailing/<int:pk>/delete', MailingDeleteView.as_view(), name='mailing_detail'),
]
