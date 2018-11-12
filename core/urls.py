from django.urls import path

from .views import ItemDetailEndpoint, ItemCreate
from .authentication import SocialLoginView
from django.conf.urls import include, url


urlpatterns = [
    path('items/<pk>/',
         ItemDetailEndpoint.as_view(),
         name='item-list'),

    path('item/create/', ItemCreate.as_view(), name='item-create'),
    path('social-login/', SocialLoginView.as_view(), name='social-login')
]
