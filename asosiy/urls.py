from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view()),
    path('product/', MahsulotView.as_view()),
    path('detail_product/', Detail_ProductView.as_view()),
    path('category/', CategoryView.as_view()),
    path('header/', HeaderView.as_view()),
    path('ichki/', IchkiView.as_view()),
    path('blank_starter/', Blank_StarterView.as_view()),
    path('components/', ComponentsView.as_view()),
    path('content/', ContentView.as_view()),
    path('listing_grid/', Listing_GridView.as_view()),
    path('listing_large/', Listing_LargeView.as_view()),
    path('offers/', OffersView.as_view()),
    path('payment/', PaymentView.as_view()),
    path('profile_adress/', Profile_AdressView.as_view()),
    path('profile_orders/', Profile_OrdersView.as_view()),
    path('profile_Seller/', Profile_SellerView.as_view()),
    path('profile_setting/', Profile_SettingView.as_view()),
    path('profile_wishlist/', Profile_WishlistView.as_view()),
    path('shopping_cart/', Shopping_CartView.as_view()),
    path('user_login/', User_LoginView.as_view()),
    path('user_register/', User_RegisterView.as_view()),



]