from django.urls import path

from .views import ItemDetailEndpoint, ItemCreate

urlpatterns = [
    path('items/<pk>/',
         ItemDetailEndpoint.as_view(),
         name='item-list'),

    path('item/create/', ItemCreate.as_view(), name='item-create'),

]
