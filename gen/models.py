from django.db import models

class Flavor(models.Model):
    name = models.CharField(max_length=200)
    salt = models.CharField(max_length=20)
    algo = models.CharField(max_length=50)
    maxlen = models.IntegerField()
    def __str__(self):
        return self.name

class Record(models.Model):
    src = models.CharField(max_length=200)
    res = models.CharField(max_length=200)
    flavor = models.ForeignKey(Flavor, on_delete=models.RESTRICT)
    def __str__(self):
        return self.res
