from django.db import models


class WorkCalendar(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()

    def __str__(self):
        return self.date



