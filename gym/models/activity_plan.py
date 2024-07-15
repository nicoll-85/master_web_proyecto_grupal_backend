from django.db import models


class ActivityPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'plan'
        verbose_name_plural = 'plans'

    def __str__(self):
        return self.name
