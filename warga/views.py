# warga/views.py
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from rest_framework import viewsets
# 🌟 IMPOR BARU UNTUK FILTERING & ORDERING
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from .serializers import WargaSerializer, PengaduanSerializer 

# ----------------------------------------------------
# VIEWS UNTUK HTML (CBV CRUD) - (Tidak berubah)
# ----------------------------------------------------

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list') 

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

# ----------------------------------------------------
# VIEWS UNTUK PENGADUAN (CBV CRUD) - (Tidak berubah)
# ----------------------------------------------------

class PengaduanListView(ListView):
    model = Pengaduan

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html' 
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

# ====================================================
# API VIEWS DENGAN DRF VIEWSETS (CRUD Penuh & Efisien)
# ====================================================

class WargaViewset(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi') 
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Dari Pertemuan 9
    
    # 🌟 KONFIGURASI FILTERING, SEARCHING, DAN ORDERING (Pertemuan 10)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat'] # Field untuk pencarian (?search=...)
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi'] # Field yang bisa diurutkan (?ordering=...)

class PengaduanViewset(viewsets.ModelViewSet):
    """API Viewset untuk Model Pengaduan (CRUD Penuh)."""
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor') 
    serializer_class = PengaduanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Dari Pertemuan 9
    
    # 🌟 KONFIGURASI FILTERING, SEARCHING, DAN ORDERING (Pertemuan 10 - Tugas Praktik)
    filter_backends = [SearchFilter, OrderingFilter]
    # Pencarian di Judul, Deskripsi, dan Nama Pelapor (relasi ForeignKey)
    search_fields = ['judul', 'deskripsi', 'pelapor__nama_lengkap'] 
    ordering_fields = ['status', 'tanggal_lapor', 'judul']
    
    def get_renderer_context(self):
        context = super().get_renderer_context()
        
        # Cek apakah request sukses membuat data (HTTP 201 Created)
        if context.get('response') and context['response'].status_code == 201:
            # Inject JavaScript untuk me-reset URL dan me-reload halaman
            context['post_form_html'] = (
                '<script>'
                'window.history.replaceState({}, document.title, window.location.pathname);'
                'window.location.reload();'
                '</script>'
            )
        return context