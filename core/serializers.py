from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        exclude = []


class ItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        exclude = []
