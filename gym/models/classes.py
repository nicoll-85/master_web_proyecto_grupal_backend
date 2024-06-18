from django.db import models

class Classes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TimeField()
    day_week = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    plan = models.ForeignKey('ClassPlan', on_delete=models.CASCADE)
    modality = models.ForeignKey('ClassModality', on_delete=models.CASCADE)

    def __str__(self):
        return self.name