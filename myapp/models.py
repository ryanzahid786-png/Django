from django.db import models


class Task(models.Model):
    """A simple to-do task saved in the database."""

    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
