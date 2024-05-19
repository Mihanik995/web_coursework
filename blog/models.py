from django.db import models
from django.utils.translation import gettext_lazy as _

from mailing.models import NULLABLE


class Post(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=100)
    body = models.TextField(verbose_name=_('post text'))
    image = models.ImageField(upload_to='blog/', verbose_name=_('image'), **NULLABLE)

    views = models.IntegerField(verbose_name=_('views count'), default=0)
    publication_date = models.DateTimeField(verbose_name=_('publication date'), auto_now_add=True)

    def __str__(self):
        if len(self.body) <= 200:
            return self.body
        else:
            return f'{self.body[:200]}...'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

