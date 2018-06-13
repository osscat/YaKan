from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
    #  list_display = ('id', 'title',)       # 一覧に表示したい項目
    #  list_display_links = ('id', )  # リンクを表示する項目
