from datetime import datetime, timezone, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from mailing.forms import MailingForm, MailingMessageForm, ClientForm
from mailing.models import Mailings, MailingMessage, Client

scheduler = BackgroundScheduler()


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailings
    template_name = 'mailing/main.html'


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailings
    template_name = 'mailing/mailing_details.html'


class MailingMessageDetailView(LoginRequiredMixin, DetailView):
    model = MailingMessage
    template_name = 'mailing/mailing_message_details.html'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'mailing/client_details.html'


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailings
    template_name = 'mailing/add_mailing.html'
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.owner = self.request.user
            if datetime.now(timezone.utc) + timedelta(hours=3) < new_mailing.first_mailing:
                new_mailing.next_mailing_date = new_mailing.first_mailing
            else:
                new_mailing.next_mailing_date = (datetime.now()
                                                 .replace(second=0, microsecond=0, tzinfo=timezone.utc))
            new_mailing.save()

        return super().form_valid(form)


class MailingMessageCreateView(LoginRequiredMixin, CreateView):
    model = MailingMessage
    template_name = 'mailing/add_mailing.html'
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing_message = form.save()
            new_mailing_message.owner = self.request.user
            new_mailing_message.save()

        return super().form_valid(form)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'mailing/add_mailing.html'
    form_class = ClientForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.owner = self.request.user
            new_client.save()

        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailings
    template_name = 'mailing/add_mailing.html'
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMessage
    template_name = 'mailing/add_mailing.html'
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:mailing_list')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'mailing/add_mailing.html'
    form_class = ClientForm
    success_url = reverse_lazy('mailing:mailing_list')


def mailing_delete(request, pk):
    mailing_to_delete = Mailings.objects.get(pk=pk)
    mailing_to_delete.delete()
    return HttpResponseRedirect(reverse_lazy('mailing:mailing_list'))


def mailing_message_delete(request, pk):
    mailing_message_to_delete = MailingMessage.objects.get(pk=pk)
    mailing_message_to_delete.delete()
    return HttpResponseRedirect(reverse_lazy('mailing:mailing_list'))


def client_delete(request, pk):
    client_to_delete = Client.objects.get(pk=pk)
    client_to_delete.delete()
    return HttpResponseRedirect(reverse_lazy('mailing:mailing_list'))


def mailing_stop(request, pk):
    mailing_to_stop = Mailings.objects.get(pk=pk)
    mailing_to_stop.is_launched = False
    mailing_to_stop.save()
    return HttpResponseRedirect(reverse_lazy('mailing:mailing_list'))


def mailing_finish(request, pk):
    mailing_to_finish = Mailings.objects.get(pk=pk)
    mailing_to_finish.is_launched = False
    mailing_to_finish.is_finished = True
    mailing_to_finish.save()
    return HttpResponseRedirect(reverse_lazy('mailing:mailing_list'))


def mailing_launch(request, pk):
    mailing_to_delete = Mailings.objects.get(pk=pk)
    mailing_to_delete.is_launched = True
    mailing_to_delete.save()
    return HttpResponseRedirect(reverse_lazy('mailing:mailing_list'))
