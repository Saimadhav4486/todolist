from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Task(models.Model):
    tasktitle = models.CharField(max_length=100, default = 'none')
    taskDesc = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True) 
    tags = models.ManyToManyField(Tag)
    status_choices = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='OPEN')
    def __str__(self):
        return self.tasktitle


    
