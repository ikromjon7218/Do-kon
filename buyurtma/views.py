from django.shortcuts import render, redirect
from django.views import View
from buyurtma.models import *
from asosiy.models import *
from userapp.models import *
from .models import *
from django.db.models import *
class SavatView(View):
    def get(self, request):
        savatlar = Savat.objects.filter(profil__user=request.user)
        summa = savatlar.aggregate(Sum('umumiy')).get('umumiy__sum')
        chegirmalar = 0
        for savat in savatlar:
            chegirmalar += savat.miqdor*(savat.mahsulot.chegirma*savat.mahsulot.narx) / 100
        content = {
            'savatlar': savatlar,
            'summa': summa,
            'chg': round(chegirmalar, 2),
            'yakuniy': summa - round(chegirmalar, 2),
        }
        return render(request, 'page-shopping-cart.html', content)

class MiqdorQoshView(View):
    def get(self, request, son):
        s1 = Savat.objects.get(id=son)
        if s1.profil.user == request.user:
            s1.miqdor += 1
            s1.umumiy += s1.mahsulot.narx
            s1.save()
        return redirect('/buyurtma/savat/')

class MiqdorKamView(View):
    def get(self, request, son):
        s1 = Savat.objects.get(id=son)
        if s1.profil.user == request.user and s1.miqdor != 1:
            s1.miqdor -= 1
            s1.umumiy -= s1.mahsulot.narx
            s1.save()
        return redirect('/buyurtma/savat/')

class BuyurtmaView(View):
    def get(self, request):
        data = {'buyurtmalar': Tanlangan.objects.filter(user=request.user),
                'profil': Profil.objects.get(user=request.user)}
        return render(request, 'page-profile-orders.html', data)

class TanlanganView(View):
    def get(self, request):
        data = {'tanlanganlar': Tanlangan.objects.all()}
        return render(request, 'page-profile-wishlist.html', data)