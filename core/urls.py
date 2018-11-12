from django.urls import path

from .views import ItemDetailEndpoint, ItemCreate
from .authentication import FacebookLogin
from django.conf.urls import include, url


urlpatterns = [
    path('items/<pk>/',
         ItemDetailEndpoint.as_view(),
         name='item-list'),

    path('item/create/', ItemCreate.as_view(), name='item-create'),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),

]
