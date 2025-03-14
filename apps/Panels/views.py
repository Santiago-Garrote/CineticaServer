from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from apps.Panels.models import *
from apps.Panels.serializers import *


# Create your views here.

#View used to @GET all panels
class ListPanelView(ListAPIView):
    queryset = Panel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPanelSerializer

#View used to @GET all sectional panels
class ListSectionalPanelView(ListAPIView):
    queryset = SectionalPanel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListSectionalPanelSerializer

#View used to @GET all sectional panels filtered by business
class ListFilteredSectionalPanelView(ListAPIView):
    queryset = SectionalPanel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListSectionalPanelSerializer

    def get_queryset(self):
        business_id = self.kwargs['business_id']
        return SectionalPanel.objects.filter(business_id=business_id)

#View used to @PATCH a sectional panel
class UpdateSectionalPanelView(UpdateAPIView):
    queryset = SectionalPanel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateSectionalPanelSerializer

#View used to @POST a sectional panel
class CreateSectionalPanelView(CreateAPIView):
    queryset = SectionalPanel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateSectionalPanelSerializer

#View used to @GET all principal panels
class ListPrincipalPanelView(ListAPIView):
    queryset = PrincipalPanel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPrincipalPanelSerializer

# View used to @GET all principal panels filtered by business
class ListFilteredPrincipalPanelView(ListAPIView):
    queryset = PrincipalPanel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPrincipalPanelSerializer

    def get_queryset(self):
        business_id = self.kwargs['business_id']
        return PrincipalPanel.objects.filter(business_id=business_id)

#View used to @PATCH a sectional panel
class UpdatePrincipalPanelView(UpdateAPIView):
    queryset = PrincipalPanel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePrincipalPanelSerializer

#View used to @POST a principal panel
class CreatePrincipalPanelView(CreateAPIView):
    queryset = PrincipalPanel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreatePrincipalPanelSerializer