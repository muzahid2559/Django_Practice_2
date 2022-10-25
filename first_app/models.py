from django.db import models

# Create your models here.

# django Models
class Musician(models.Model):
    # id = models.AutoField(primary_key=True) ...{hidden column auto make django}
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=30)


class Album(models.Model):
    # id = models.AutoField(primary_key=True) ...{hidden column auto make django}
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
