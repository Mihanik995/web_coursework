from django.contrib import admin

from mailing.models import Mailings, MailingMessage, Client


@admin.register(Mailings)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_mailing', 'frequency', 'owner')


@admin.register(MailingMessage)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'body')


@admin.register(Client)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email')
