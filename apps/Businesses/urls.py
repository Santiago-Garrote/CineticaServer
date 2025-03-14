from django.urls import path
from .views import *

urlpatterns = [
    path('', ListBusiness.as_view(), name='listBusinesses'),
    path('new/', CreateBusiness.as_view(), name='createBusiness'),
]