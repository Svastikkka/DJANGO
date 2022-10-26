from django.db import models


# Create your models here.

class users(models.Model):
    first_name = models.CharField(max_length=256, unique=True, default='SOME STRING')
    last_name = models.CharField(max_length=256, unique=True, default='SOME STRING')
    email = models.CharField(max_length=256, unique=True, default='SOME STRING')

    def __str__(self):
        return self.first_name
