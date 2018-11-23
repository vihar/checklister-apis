from django.urls import path

from .views import ItemDetailEndpoint, ItemCreate, StatusView, ItemListAPIView
from .authentication import SocialLoginView


urlpatterns = [
    path('', StatusView.as_view(), name='status'),
    path('items/<pk>/', ItemDetailEndpoint.as_view(), name='item-list'),
    path('item/create/', ItemCreate.as_view(), name='item-create'),
    path('item-list/', ItemListAPIView.as_view(), name='item-list'),
    path('social-login/', SocialLoginView.as_view(), name='social-login')
]
