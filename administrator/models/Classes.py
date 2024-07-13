from django.db import models

class Classes(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'class'
        verbose_name_plural = 'classes'

    def __str__(self):
        return self.name