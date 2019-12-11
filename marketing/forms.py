# -*- coding: utf-8 -*-

from smtplib import SMTPException

from django import forms
from django.core.mail import EmailMessage
from .models import Contact


class ContactForm(forms.ModelForm):
    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "Name *", 'required': ""}),
    )
    

    class Meta:
        model = Contact
        fields = ('email',)