# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MailTemplate(models.Model):
    template = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/mailguner/images/")
    created_at = models.DateTimeField(auto_now_add=True)

    # def __unicode__(self):
    #     return self.id

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    template = models.ForeignKey(MailTemplate, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sender")
    recipients = models.ManyToManyField(User, related_name="recipients")
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
