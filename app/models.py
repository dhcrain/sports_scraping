from django.db import models

# Create your models here.

class NflSearch(models.Model):
    player_bio = models.TextField()
    stats = models.TextField()
    player_name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
