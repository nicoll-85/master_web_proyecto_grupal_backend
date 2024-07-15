from django.db import models

from gym.models.activity import Activity


class UsersActivities(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        ordering = ['client']
        verbose_name = 'user_activity'
        verbose_name_plural = 'user_activities'
        unique_together = ['client', 'activity']

    def __str__(self):
        return f"{self.client.username} - {self.activity}"
