from django.db import models
from django.contrib.auth.models import User
from asosiy.models import Mahsulot
class Profil(models.Model):
    J = [('erkak', 'erkak'),
        ('ayol', 'ayol')]
    ism = models.CharField(max_length=100)
    jins = models.CharField(max_length=5, choices=J, null=True)
    shahar = models.CharField(max_length=100)
    davlat = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}"

class Izoh(models.Model):
    baho = models.FloatField()
    matn = models.CharField(max_length=900)
    sana = models.DateField(auto_now=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, null=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.baho}"