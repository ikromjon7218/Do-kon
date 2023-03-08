from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('', LoginView.as_view()),
    path('logout/', Logoutview.as_view()),
]