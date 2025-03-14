from django.urls import path
from .views import *

urlpatterns = [
    path('', ListTool.as_view(), name='listTools'),
    path('new/', CreateTool.as_view(), name='createTool'),
]