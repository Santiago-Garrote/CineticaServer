from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView
from apps.Businesses.models import Business
from apps.Businesses.serializers import GetBusinessSerializer, PostBusinessSerializer


# Create your views here.

#View used to @GET Business
class ListBusiness(ListAPIView):
    queryset = Business.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetBusinessSerializer

#View used to @POST Business
class CreateBusiness(CreateAPIView):
    queryset = Business.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostBusinessSerializer