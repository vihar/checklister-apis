from rest_framework.response import Response
from rest_framework import status

from django.http import Http404
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated

from .models import Item
from .serializers import ItemSerializer, ItemListSerializer


class StatusView(APIView):
    def get(self, request):
        up = {'Status': 'API Server Working 🚀'}
        # down = {'status': 'system down and broken!'}
        return Response(up)


class ItemCreate(APIView):
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailEndpoint(APIView):

    def get_object(self, pk, **kwargs):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response({"message": "Deleted"})


class ItemListAPIView(APIView):
    def get_object(self, **kwargs):
        try:
            return Item.objects.all()
        except Item.DoesNotExist:
            raise status.Http404

    def get(self, request, **kwargs):
        items = self.get_object()
        serializer = ItemListSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemListSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
