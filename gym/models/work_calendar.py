from django.db import models


class WorkCalendar(models.Model):
    date = models.DateField()

    class Meta:
        ordering = ['date']
        verbose_name = 'calendar'
        verbose_name_plural = 'calendars'

    def __str__(self):
        return self.date
