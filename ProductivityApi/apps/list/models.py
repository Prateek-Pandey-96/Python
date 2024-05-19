from django.db import models
from apps.util.models import Timestamps
from django.contrib.auth import get_user_model

class List(Timestamps, models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500,null=True)
    
    def __str__(self):
        return self.name
    
class ListItem(Timestamps, models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text