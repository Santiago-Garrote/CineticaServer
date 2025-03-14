from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView
from apps.Tools.models import Tool
from apps.Tools.serializers import ListToolSerializer, CreateToolSerializer


# Create your views here.

#View used to @GET Business
class ListTool(ListAPIView):
    queryset = Tool.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListToolSerializer

#View used to @POST Business
class CreateTool(CreateAPIView):
    queryset = Tool.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateToolSerializer
