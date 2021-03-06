from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Project, ProjectMember, Lane, Task, Label


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'owner_id', 'status')


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ('id', 'project_id', 'user_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')


class LaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lane
        fields = ('id', 'project_id', 'title', 'status', 'order')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'order', 'user_id', 'man_day', 'status', 'lane_id', 'label_id', 'delete_flag')


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'name', 'color')
