# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from mail_sander.models import Message, MailTemplate


admin.site.register(Message)
admin.site.register(MailTemplate)
