from django.db import models
# from django.contrib.auth.models import User

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):
        return f"{self.nom}"

class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.FloatField()
    brend = models.CharField(max_length=50)
    davlat = models.CharField(max_length=50)
    kafolat = models.CharField(max_length=50)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    min_miqdor = models.PositiveSmallIntegerField(default=1)
    tasdiqlangan = models.BooleanField(default=True)
    yetkazish = models.CharField(max_length=20, default='3-4 kun')
    mavjud = models.BooleanField(default=True)
    chegirma = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return f"{self.nom}"

class Media(models.Model):
    rasm = models.FileField(upload_to='mahsulotlar')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.mahsulot}"