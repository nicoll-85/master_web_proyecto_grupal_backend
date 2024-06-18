from django.db import models

class ClassSchedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_week = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class_id = models.ForeignKey('Classes', on_delete=models.CASCADE)
    user_id = models.ForeignKey('authentication.User', on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.class_id.name} - {self.day_week}"