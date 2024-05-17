from django import forms

from mailing.models import Mailings, MailingMessage, Client


class MailingForm(forms.ModelForm):
    first_mailing = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    frequency = forms.ChoiceField(choices=(('1 day', 'One day'), ('7 days', 'One week'), ('30 days', 'One month')))

    class Meta:
        model = Mailings
        fields = ('first_mailing', 'frequency', 'mailing_message', 'mailing_clients')
        widgets = {
            'mailing_clients': forms.CheckboxSelectMultiple()
        }


class MailingMessageForm(forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = ('theme', 'body',)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('email', 'name', 'surname', 'notes')
