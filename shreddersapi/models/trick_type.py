from django.db import models

class TrickType(models.Model):
    
    label = models.CharField(max_length=20)