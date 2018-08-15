from django.db import models


class Project(models.Model):
    title = models.TextField(blank=False)
    description = models.TextField(blank=True)
    owner_id = models.IntegerField(blank=False)
    status = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.title


class ProjectMember(models.Model):
    project_id = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=False)


class Lane(models.Model):
    project_id = models.IntegerField(blank=False)
    title = models.TextField(blank=False)
    status = models.IntegerField(default=0, blank=False)
    order = models.IntegerField(blank=False)


class Task(models.Model):
    title = models.TextField(blank=False)
    order = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=True,null=True)
    man_day = models.FloatField(blank=False)
    status = models.IntegerField(default=0, blank=False)
    lane_id = models.IntegerField(blank=False)
    label_id = models.IntegerField(blank=True,null=True)
    delete_flag = models.IntegerField(default=0, blank=False)


class Label(models.Model):
    name = models.TextField(blank=False)
    color = models.CharField(blank=False, max_length=6)