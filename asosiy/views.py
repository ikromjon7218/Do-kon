from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.views import View

class RegisterView(View):
    def post(self, request):
        if request.POST.get('p') == request.POST.get('cp'):
            User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p'))
            return redirect('/asosiy/')
        return redirect('/')
    def get(self, request):
        return render(request, 'page-user-register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        f = authenticate(username=request.POST.get('username'), password=request.POST.get('p'))
        if f is None:
            return redirect('/')
        login(request, f)
        return redirect('/asosiy/')

class Logoutview(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class Home2View(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {'chegirmalilar': Mahsulot.objects.all()[:7],
                    'bolimlar': Bolim.objects.all()[:7]}
            return render(request, 'page-index.html', data)
        return redirect('/')
class MahsulotView(View):
    pass

class Detail_ProductView(View):
    def get(self, request):
        return render(request, 'page-detail-product.html')

class CategoryView(View):
    def get(self, request):
        return render(request, 'page-category.html')

class HeaderView(View):
    def get(self, request):
        return render(request, 'header.html')
class IchkiView(View):
    def get(self, request):
        return render(request, 'ichki.html')
class Blank_StarterView(View):
    def get(self, request):
        return render(request, 'page-blank-starter.html')
class ComponentsView(View):
    def get(self, request):
        return render(request, 'page-components.html')
class ContentView(View):
    def get(self, request):
        return render(request, 'page-content.html')
class Listing_GridView(View):
    def get(self, request):
        return render(request, 'page-listing-grid.html')
class Listing_LargeView(View):
    def get(self, request):
        return render(request, 'page-listing-large.html')
class OffersView(View):
    def get(self, request):
        return render(request, 'page-offers.html')
class PaymentView(View):
    def get(self, request):
        return render(request, 'page-payment.html')
class Profile_AdressView(View):
    def get(self, request):
        return render(request, 'page-profile-address.html')
class Profile_MainView(View):
    def get(self, request):
        return render(request, 'page-profile-main.html')
class Profile_OrdersView(View):
    def get(self, request):
        return render(request, 'page-profile-orders.html')
class Profile_SellerView(View):
    def get(self, request):
        return render(request, 'page-profile-seller.html')
class Profile_SettingView(View):
    def get(self, request):
        return render(request, 'page-profile-setting.html')
class Profile_WishlistView(View):
    def get(self, request):
        return render(request, 'page-profile-wishlist.html')
class Shopping_CartView(View):
    def get(self, request):
        return render(request, 'page-shopping-cart.html')
class User_LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')
class User_RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')
