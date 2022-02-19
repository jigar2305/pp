from operator import mod
from django.db import models

# Create your models here.
class task(models.Model):
    t_name = models.CharField(max_length=100)
    t_desc = models.CharField(max_length=200)
    class meta:
        db_table = 'task'