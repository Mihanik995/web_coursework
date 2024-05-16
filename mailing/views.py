from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from mailing.forms import MailingForm
from mailing.models import Mailings


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailings
    template_name = 'mailing/main.html'

class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailings
    template_name = 'mailing/mailing_details.html'

class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailings
    template_name = 'mailing/add_mailing.html'
    form_class = MailingForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.owner = self.request.user
            new_mailing.save()

        return super().form_valid(form)
