from django.db import models


class Project(models.Model):
    title = models.TextField(blank=False)
    description = models.TextField(blank=True)
    owner_id = models.IntegerField(blank=False)
    status = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.title


