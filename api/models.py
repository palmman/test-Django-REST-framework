from django.db import models

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=99)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    class Meta:
        ordering = ['-date_created']
        db_table = 'task'
    
    def __str__(self):
        return self.title