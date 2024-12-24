from django.db import models


class Task(models.Model):
  text = models.TextField(max_length=100, blank=True, null=True)

  def __str__(self):
        return self.text

