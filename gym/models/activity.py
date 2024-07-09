from django.db import models

from gym.models.activity_modality import ActivityModality
from gym.models.activity_plan import ActivityPlan


class Activity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    plan = models.ForeignKey(ActivityPlan, on_delete=models.CASCADE)
    modality = models.ForeignKey(ActivityModality, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = 'activity'
        verbose_name_plural = 'activities'

    @property
    def schedules(self):
        return self.activityschedule_set.all()

    def __str__(self):
        return self.name
