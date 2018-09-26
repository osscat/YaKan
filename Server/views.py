from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Project, ProjectMember, Lane, Task, Label
from .serializer import ProjectSerializer, ProjectMemberSerializer, UserSerializer, LaneSerializer, TaskSerializer, \
    LabelSerializer
from django.http.response import JsonResponse
from django.core import serializers


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


class ProjectViewSet2(viewsets.ModelViewSet):
    queryset = Project.objects.raw(
        'select * from public."Server_project" where id IN (select distinct project_id from public."Server_projectmember" where user_id = ''%s'')'
        , ["3"]
    )
    serializer_class = ProjectSerializer

    @action(methods=['get'], detail=False)
    def filter(self, request):
        title = request.GET.get('title')
        if title:
            ret = Project.objects.raw(
              'select * from public."Server_project"' +
              ' where id IN (select distinct project_id from public."Server_projectmember" where user_id = %s)' +
              ' and title like %s'
              , [request.GET.get('user_id'), '%' + title + '%']
            )
        else:
            ret = Project.objects.raw(
                'select * from public."Server_project"' +
                ' where id IN (select distinct project_id from public."Server_projectmember" where user_id = %s)'
                , [request.GET.get('user_id')]
            )
        ret_json = '['
        cnt = 0
        for p in ret:
            if cnt != 0:
                ret_json += ','
            cnt = cnt + 1
            ret_json += '{' \
                        '"id" : "' + str(p.pk) + '",' \
                        '"title" : "' + p.title + '",' \
                        '"description" : "' + p.description + '",' \
                        '"owner_id" : "' + str(p.owner_id) + '",' \
                        '"status" : "' + str(p.status) + '"' \
                        '}'
        ret_json += ']'
        return Response(ret_json)


class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    filter_fields = ('project_id',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class LaneViewSet(viewsets.ModelViewSet):
    queryset = Lane.objects.all().order_by('order')
    serializer_class = LaneSerializer
    filter_fields = ('project_id',)


class TaskViewSet(viewsets.ModelViewSet):
    FLAG_EXISTS = 0
    FLAG_DELETED = 9

    queryset = Task.objects.filter(delete_flag=FLAG_EXISTS).order_by('order')
    serializer_class = TaskSerializer
    filter_fields = ('lane_id',)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete_flag = self.FLAG_DELETED
        task.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=False)
    def bulk_delete(self, request):
        lane_id = request.data['lane_id']
        Task.objects.filter(lane_id=lane_id).update(delete_flag=self.FLAG_DELETED)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
