from django.db import models

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('alpha', 'Important'),
        ('beta', 'Somewhat Important'),
        ('omega', 'Less Important'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority_level = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
