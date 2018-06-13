from rest_framework import routers
from .views import ProjectViewSet, ProjectMemberViewSet, UserViewSet, LaneViewSet, TaskViewSet, LabelViewSet


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'projectmembers', ProjectMemberViewSet)
router.register(r'users', UserViewSet)
router.register(r'lanes', LaneViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'labels', LabelViewSet)
