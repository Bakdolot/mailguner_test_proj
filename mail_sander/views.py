# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.utils import timezone

from mail_sander.forms import CustomUserCreationForm, MessageForm
from mail_sander.models import MailTemplate
from mail_sander.tasks import send_email_task


class RegisterView(View):
    def get(self, request):
        return render(
            request, "users/register.html", {"form": CustomUserCreationForm, "user": request.user}
        )

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("login"))
        return redirect(reverse("register"))


class MainView(View):
    def get(self, request):
        templates = MailTemplate.objects.all()
        context = {"form": MessageForm, "templates": templates}
        return render(request, "main.html", context)

    def post(self, request):
        form = MessageForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR, "Invalid form")
            return redirect(reverse("main"))
        message = form.save(commit=False)
        message.sender = request.user
        message.save()
        recipients = form.cleaned_data["recipients"]

        sent_at = message.sent_at

        sent_at = sent_at if timezone.now() < sent_at else None

        for recipient in recipients:
            send_email_task.apply_async(
                (message.id, recipient.id, message.template.template), eta=sent_at
            )
        messages.add_message(request, messages.SUCCESS, "Message sent")
        return redirect(reverse("main"))
