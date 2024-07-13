from django.db import models


class ActivityModality(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'modality'
        verbose_name_plural = 'modalities'

    def __str__(self):
        return self.name
