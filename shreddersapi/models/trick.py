from django.db import models
from shreddersapi.models.skater import Skater
from shreddersapi.models.trick_type import TrickType

class Trick(models.Model):
    
    trick_type = models.ForeignKey(TrickType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    skater = models.ForeignKey(Skater, on_delete=models.CASCADE)
    skill_level = models.IntegerField()