from django.db import models
from gym.models.activity import Activity


class ActivitySchedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_week = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    coach = models.ForeignKey('authentication.User', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['day_week']
        verbose_name = 'schedule'
        verbose_name_plural = 'schedules'

    def __str__(self):
        return f"{self.activity.name} - {self.day_week} - {self.start_time} - {self.end_time}"
