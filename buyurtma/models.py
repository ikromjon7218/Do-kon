from django.db import models
from asosiy.models import *
from django.contrib.auth.models import User
from userapp.models import *

class Tanlangan(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.mahsulot}"
class Buyurtma(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, null=True)
    sana = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.mahsulot}"
class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    umumiy = models.PositiveIntegerField(null=True)
    miqdor = models.PositiveIntegerField(null=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.mahsulot}"