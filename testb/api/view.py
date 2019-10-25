#from rest_framework.generics import ListAPIView, RetrieveAPIView
from testb.models import Test
from .serializers import testserializers
from rest_framework import viewsets, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class testviewset(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = testserializers

    def perform_update(self, serializer):
        serializer.save()

'''

from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)


class testListView(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = testserializers
    permission_classes = (permissions.AllowAny, )


class testDetailView(RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = testserializers
    permission_classes = (permissions.AllowAny, )


class testCreateView(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = testserializers
    permission_classes = (permissions.AllowAny, )


class testUpdateView(UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = testserializers
    permission_classes = (permissions.AllowAny, )


class testDeleteView(DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = testserializers
    permission_classes = (permissions.AllowAny, )
'''