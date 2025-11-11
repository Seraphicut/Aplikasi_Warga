# warga/api_urls.py
from django.urls import path
from .views import WargaListAPIView, PengaduanListAPIView

urlpatterns = [
    # Ganti 'warga/' menjadi string kosong ''
    path('', WargaListAPIView.as_view(), name='api-warga-list'),
    
    # Endpoint Pengaduan sekarang akan ada di: /api/pengaduan/
    path('pengaduan/', PengaduanListAPIView.as_view(), name='api-pengaduan-list'),
]