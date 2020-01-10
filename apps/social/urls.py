
from django.urls import path, include

from apps.social.views import (ReviewCreateView,
                                      ReviewDetailView,
                                      SocialProfileDetailView,
                                      SocialProfileSelfDetailView,
                                      # SocialProfileListView,
                                      SocialProfileUpdateView)


app_name = 'social'
urlpatterns = [
    # path('', SocialProfileListView.as_view(), name='list'),
    path('profile/', SocialProfileSelfDetailView.as_view(), name='detail'),
    path('profile/(?P<slug>[-\w]+)/', SocialProfileDetailView.as_view(), name='detail'),

    # Profile is updated in settings
    path('settings/profile/', SocialProfileUpdateView.as_view(), name='update'),

    # Review urls
    path('reviews/new/(?P<slug>[-\w]+)/', ReviewCreateView.as_view(), name='new_review'),
    path('reviews/(?P<slug>[-\w]+)/', ReviewDetailView.as_view(), name='review_detail'),
]
