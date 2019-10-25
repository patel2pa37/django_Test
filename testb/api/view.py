
from testb.models import Test #from django model
from .serializers import testserializers #from serializer model
#prebuild viewsets
from rest_framework import viewsets, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

'''
view class is created after serializers,
rather then building a custome view, 
use prebuild viewsets
'''

#the MoldeViewSet allow fuctionality such as create, delete, update, retrive
class testviewset(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = testserializers

    def perform_update(self, serializer):
        serializer.save()

#bottom code does samething as the above code, above code more efficient
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