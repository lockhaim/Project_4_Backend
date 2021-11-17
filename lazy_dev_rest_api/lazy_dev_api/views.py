from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import GuideSerializer
from .models import Guide

class GuideList(generics.ListCreateAPIView):
    queryset = Guide.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = GuideSerializer # tell django what serializer to use

class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all().order_by('id')
    serializer_class = GuideSerializer
