from django.db import models

class UsersClasses(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    class_id = models.ForeignKey('Classes', on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.class_id.name} - {self.day_week}"