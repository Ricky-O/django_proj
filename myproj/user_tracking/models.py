import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    access_date = models.DateTimeField('date accessed')
    access_url = models.CharField(max_length=200)
    def __str__(self):
        return self.user_name
    def was_accessed_recently(self):
        return self.access_date >= timezone.now() - datetime.timedelta(hours=1)
    def get_url(self):
        return self.access_url

class Access(models.Model):
    user = models.ForeignKey(User)
    access_text = models.CharField(max_length=200)
    hits = models.IntegerField(default=0)
    def __str__(self):
        return self.access_text

