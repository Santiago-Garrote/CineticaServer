from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import *

# Create your views here.

#View used to @GET all sectors
class ListSectorsView(ListAPIView):
    queryset = Sector.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListSectorSerializer

#View used to @GET all sectors filtered by business id
class ListFilteredSectorsView(ListAPIView):
    queryset = Sector.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListSectorSerializer

    def get_queryset(self):
        business_id = self.kwargs['business_id']
        return Sector.objects.filter(Business_id=business_id)

#View used to @POST a sectors
class CreateSectorsView(CreateAPIView):
    queryset = Sector.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateSectorSerializer
