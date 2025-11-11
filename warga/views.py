# warga/views.py

from .models import Warga, Pengaduan
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
# Perhatikan: Anda sudah mengimpor .models dua kali, 
# tapi itu tidak menyebabkan error fatal. Kita fokus pada yang DRF.
from .forms import WargaForm, PengaduanForm

# --- IMPORT DRF ---
from rest_framework.generics import ListAPIView
from .serializers import WargaSerializer, PengaduanSerializer

# ----------------------------------------------------
# VIEWS UNTUK WARGA (CRUD Penuh)
# ----------------------------------------------------

class WargaListView(ListView):
    # Pertemuan 1: ListView (R)
    model = Warga

class WargaDetailView(DetailView):
    # Pertemuan 1: DetailView (R) - Challenge
    model = Warga

class WargaCreateView(CreateView):
    # Pertemuan 3: CreateView (C)
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    # Pertemuan 4: UpdateView (U)
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    # Pertemuan 4: DeleteView (D)
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

# ----------------------------------------------------
# VIEWS UNTUK PENGADUAN (Challenge Pertemuan 2, 3, 4)
# ----------------------------------------------------

class PengaduanListView(ListView):
    # Pertemuan 2: ListView untuk Pengaduan
    model = Pengaduan

class PengaduanCreateView(CreateView):
    # Pertemuan 3: CreateView untuk Pengaduan
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanUpdateView(UpdateView):
    # Pertemuan 4: UpdateView untuk Pengaduan - Challenge
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html' 
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    # Pertemuan 4: DeleteView untuk Pengaduan - Challenge
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

# ====================================================
# API VIEWS DENGAN DJANGO REST FRAMEWORK (DRF)
# ====================================================

class WargaListAPIView(ListAPIView):
    # Tugas Pertemuan 6: ListAPIView untuk Daftar Warga
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class PengaduanListAPIView(ListAPIView):
    # Tambahan: ListAPIView untuk Daftar Pengaduan
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer