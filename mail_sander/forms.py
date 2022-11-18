# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, widgets
from django import forms

from mail_sander.models import Message


class MessageForm(ModelForm):
    sent_at = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=widgets.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    class Meta:
        model = Message
        fields = ["title", "body", "recipients", "template", "sent_at"]


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
