from django.shortcuts import render
from rest_framework import viewsets
from restaurants.models import Mac, Menu
from .serializers import MacSerializers


class MacAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Mac.objects.all()
    serializer_class = MacSerializers
