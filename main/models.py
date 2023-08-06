from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    categories_option = ["Fashion","Business","Travel","Cricket","Others"]
    title = models.TextField(max_length=256)
    description = models.TextField(max_length=256)
    category = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=datetime.now(), blank=True)
