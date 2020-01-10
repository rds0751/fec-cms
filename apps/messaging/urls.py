from django.conf.urls import url
from django.urls import path, include

from apps.messaging.views import (MessageCreateView,
                                        MessageDetailView,
                                        MessageListView,
                                        )


app_name = 'messaging'
urlpatterns = [
    path('', MessageListView.as_view(), name='inbox'),
    path('new/(?P<slug>[-\w]+)', MessageCreateView.as_view(), name='new'),
    path('(?P<slug>[-\w]+)/', MessageDetailView.as_view(), name='detail'),
]
