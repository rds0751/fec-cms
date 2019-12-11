# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import contact, contacts

urlpatterns = [
    url(r'^$', contact, name='contact'),
    url(r'^contacts-list/', contacts, name='contacts'),
]
