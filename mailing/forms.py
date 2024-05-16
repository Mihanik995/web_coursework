from django import forms

from mailing.models import Mailings


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailings
        fields = ('first_mailing', 'frequency', 'mailing_message', 'mailing_clients')
