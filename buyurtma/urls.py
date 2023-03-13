from django.urls import path
from .views import *

urlpatterns = [
    path('savat/', SavatView.as_view()),
    path('savat_q/<int:son>/', MiqdorQoshView.as_view()),
    path('savat_k/<int:son>/', MiqdorKamView.as_view()),

    path('buyurtma/', BuyurtmaView.as_view()),

    path('tanlangan/', TanlanganView.as_view()),
]