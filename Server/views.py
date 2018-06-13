from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import Project
from .serializer import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
