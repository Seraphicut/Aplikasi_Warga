from django.urls import path
from .views import (
    WargaListView, WargaDetailView, WargaCreateView, WargaUpdateView, WargaDeleteView,
    PengaduanListView, PengaduanCreateView, PengaduanUpdateView, PengaduanDeleteView
)

urlpatterns = [
    # URL WARGA (CRUD)
   path('', WargaListView.as_view(), name='warga-list'), 
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), 
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    
    # 🚨 PERBAIKI INI: Ganti name='warga-edit' menjadi 'warga-update'
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-update'), 
    
    # 🚨 JUGA PERBAIKI INI: Ganti name='warga-hapus' menjadi 'warga-delete'
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-delete'),

    # URL PENGADUAN 
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'), 
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'), 
    
    # 🌟 PERBAIKI: Ganti name='pengaduan-edit' menjadi 'pengaduan-update'
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-update'), 
    
    # 🌟 PERBAIKI: Ganti name='pengaduan-hapus' menjadi 'pengaduan-delete'
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-delete'), 
]