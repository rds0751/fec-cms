# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages

from .models import Contact

from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        model = Contact()
        model.email = request.POST['email']
        model.save()

    return render(request, 'pages/index.html', {})

def contacts(request):
    items = Contact.objects.all()
    return render(request, 'contact/contacts.html', locals())