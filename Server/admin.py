from django.contrib import admin
from .models import Project, ProjectMember, User, Lane, Task, Label


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
    #  list_display = ('id', 'title',)       # 一覧に表示したい項目
    #  list_display_links = ('id', )  # リンクを表示する項目

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Lane)
class LaneAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass