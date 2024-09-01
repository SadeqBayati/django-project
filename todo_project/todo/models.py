from django.db import models


class Task(models.Model):
    TASK_CHOICES = [
        ('option1', 'TODO'),
        ('option2', 'DOING'),
        ('option3', 'DONE'),
    ]
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100, choices=TASK_CHOICES, default='TODO')

    def __str__(self):
        return self.title
