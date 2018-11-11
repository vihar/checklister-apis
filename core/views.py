from rest_framework.response import Response
from rest_framework import status

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Item
from .serializers import ItemSerializer


class ItemCreate(APIView):
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailEndpoint(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk, **kwargs):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = ItemSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = ItemSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        return Response({"message": "Delete Not Allowed"})
