from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Project, ProjectMember, Lane, Task, Label
from .serializer import ProjectSerializer, ProjectMemberSerializer, UserSerializer, LaneSerializer, TaskSerializer, \
    LabelSerializer


class ProjectFilter(filters.FilterSet):
    # フィルタの定義
    title = filters.CharFilter(name="title", lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # フィルタセットの指定
    filter_class = ProjectFilter


class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    filter_fields = ('project_id',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LaneViewSet(viewsets.ModelViewSet):
    queryset = Lane.objects.all()
    serializer_class = LaneSerializer
    filter_fields = ('project_id',)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_fields = ('lane_id',)

    @action(methods=['post'], detail=False)
    def bulk_delete(self, request):
        lane_id = request.data['lane_id']
        Task.objects.filter(lane_id=lane_id).update(delete_flag=9)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
