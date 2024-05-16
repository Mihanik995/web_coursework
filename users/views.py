from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm
from users.models import User


class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register')
