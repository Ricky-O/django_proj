from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    access_date = models.DateTimeField('date accessed')
    access_url = models.CharField(max_length=200)

class Access(models.Model):
    user = models.ForeignKey(User)
    user_text = models.CharField(max_length=200)
    hits = models.IntegerField(default=0)

    