from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='e-mail')
    name = models.CharField(verbose_name=_('name'), max_length=50)
    surname = models.CharField(verbose_name=_('surname'), max_length=50, **NULLABLE)
    notes = models.TextField(verbose_name=_('notes'), **NULLABLE)

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class MailingMessage(models.Model):
    theme = models.CharField(verbose_name=_('message theme'), max_length=100)
    body = models.TextField(verbose_name=_('message text'))

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'


class Mailings(models.Model):
    first_mailing = models.DateTimeField(verbose_name=_('first mailing time and date'))
    frequency = models.DateTimeField(verbose_name=_('frequency'))
    is_launched = models.BooleanField(verbose_name='is_launched', default=True)
    is_finished = models.BooleanField(verbose_name='is_finished', default=False)

    mailing_message = models.ForeignKey(to=MailingMessage, on_delete=models.CASCADE,
                                        verbose_name=_('mailing message'))
    mailing_clients = models.ManyToManyField(to=Client, verbose_name=_('mailing clients list'))

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'mailing'
        verbose_name_plural = 'mailings'

class MailingAttempt(models.Model):
    datetime = models.DateTimeField(verbose_name=_('mailing attempt date and time'))
    is_successful = models.BooleanField(verbose_name=_('status'))
    mail_server_response = models.TextField(verbose_name=_('mail server response'))

    mailing = models.ForeignKey(to=Mailings, on_delete=models.CASCADE)