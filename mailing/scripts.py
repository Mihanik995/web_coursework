from datetime import datetime, timezone

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import EmailMessage
from django_apscheduler.jobstores import DjangoJobStore

from config import settings
from mailing.models import Mailings


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(send_mailing, 'interval', seconds=60)
    scheduler.start()


def send_mailing():
    current_datetime = datetime.now()
    current_datetime = current_datetime.replace(second=0, microsecond=0, tzinfo=timezone.utc)
    mailings = Mailings.objects.filter(next_mailing_date=current_datetime).filter(is_launched=True).all()

    for mailing in mailings:
        email = EmailMessage(subject=mailing.mailing_message.theme,
                             body=mailing.mailing_message.body,
                             to=[client.email for client in mailing.mailing_clients.all()]
                             )
        email.send()

        mailing.next_mailing_date += mailing.frequency
        mailing.save()
