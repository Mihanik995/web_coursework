from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import UserRegisterView, activate

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='activate'),
    path('ver_request/', TemplateView.as_view(), name='ver_request'),
]
