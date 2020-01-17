from django.db import models
from django.utils import timezone
from django.core.signing import TimestampSigner
from datetime import datetime, timedelta

from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager

import re

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True,
    )
    content = MarkdownxField()
    tags = TaggableManager(
        blank=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    publish = models.BooleanField(
        default=True,
        blank=False,
    )
    hit_count = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    def get_title(self):
        return self.content.split('\n')[0].replace('#', '').strip()

    def get_content(self):
        return ''.join(self.content.split('\n')[1:])

    def get_preview(self):
        # preview = re.sub('!.+[]', '', self.content)
        text = ''.join(self.content.split('\n')[1:])
        preview = re.sub('\!\[\]\(.+\)', '', text)
        preview = re.sub('\#+', '', preview)
        return(preview)

    def __str__(self):
        return self.get_title()


class ArticleHitCount(models.Model):
    ip = models.CharField(
        max_length=16,
        default=None,
        null=True
    )
    article = models.ForeignKey(
        Article,
        default=None,
        null=True,
        on_delete=models.CASCADE
    )
    date = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
