from rest_framework import viewsets, filters

from .models import Project, ProjectMember, User, Lane, Task, Label
from .serializer import ProjectSerializer, ProjectMemberSerializer, UserSerializer, LaneSerializer, TaskSerializer, \
    LabelSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LaneViewSet(viewsets.ModelViewSet):
    queryset = Lane.objects.all()
    serializer_class = LaneSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_fields = ('lane_id',)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
