from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.Javelins.serializer import *
from .models import *


# Create your views here.

#View used to @GET all javelins
class ListJavelinsView(ListAPIView):
    queryset = Javelin.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListJavelinSerializer

#View used to @GET all javelins filtered by business
class ListFilteredJavelinsView(ListAPIView):
    queryset = Javelin.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListJavelinSerializer

    def get_queryset(self):
        sector_id = self.kwargs['sector_id']
        return Javelin.objects.filter(sector_id=sector_id)

#View used to @PATCH a javelin
class UpdateJavelinView(UpdateAPIView):
    queryset = Javelin.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateJavelinSerializer

#View used to @POST a javelin
class CreateJavelinView(CreateAPIView):
    queryset = Javelin.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateJavelinSerializer