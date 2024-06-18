from django.db import models


class Faqs(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question