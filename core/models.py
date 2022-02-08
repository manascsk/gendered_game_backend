from django.db import models

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length=100,null=True)
    event_name = models.CharField(max_length=100,null=True)
    developer_name = models.CharField(max_length=100,null=True)
    platform = models.CharField(max_length=100,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.event_name