from django.db import models


class Faqs(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        ordering = ['question']
        verbose_name = 'faq'
        verbose_name_plural = 'faqs'

    def __str__(self):
        return self.question
