from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home2View.as_view()),



    path('asosiy/', include('asosiy.urls')),
    path('userapp/', include('userapp.urls')),
    path('buyurtma/', include('buyurtma.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)