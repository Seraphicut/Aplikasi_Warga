# warga/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Hanya impor Viewset (CRUD Penuh)
from .views import WargaViewset, PengaduanViewset 

# 1. Buat Router
router = DefaultRouter()

# 2. Daftarkan Viewset Warga (URL: /api/warga/)
router.register(r'warga', WargaViewset, basename='warga')

# 3. Daftarkan Viewset Pengaduan (URL: /api/pengaduan/)
router.register(r'pengaduan', PengaduanViewset, basename='pengaduan')

# URL API sekarang sepenuhnya ditentukan oleh router.
urlpatterns = [
    # Cukup satu path ini yang mencakup semua URL yang dihasilkan Router.
    path('', include(router.urls)),
]