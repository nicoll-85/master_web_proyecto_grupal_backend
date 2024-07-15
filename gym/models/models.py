from django.db import models

class ClassPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class ClassModality(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    plan = models.ForeignKey(ClassPlan, on_delete=models.CASCADE)
    modality = models.ForeignKey(ClassModality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ClassSchedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_week = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class_ref = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='schedules')
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_ref.name} - {self.get_day_display()}"

    def get_day_display(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[self.day_week]

class UsersClasses(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    class_ref = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.class_ref.name}"
