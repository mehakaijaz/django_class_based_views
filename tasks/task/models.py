from django.db import models

# Create your models here.
"""
class Task:
date_created datetime
id int
name str
description text
"""
class Task(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    #id=models.IntegerField()
    name=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name