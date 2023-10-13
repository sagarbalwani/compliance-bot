from django.db import models

# Create your models here.

class ApiQuery(models.Model):
    query = models.TextField(max_length = 500, null = False, blank = False)