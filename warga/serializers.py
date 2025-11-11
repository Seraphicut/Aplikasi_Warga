# warga/serializers.py
from rest_framework import serializers
from .models import Warga, Pengaduan # PASTIKAN MODEL PENGADUAN SUDAH DI-IMPORT

# Serializer untuk Model Warga (sudah ada)
class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon', 'tanggal_registrasi']

# Serializer untuk Model Pengaduan (INI YANG HILANG ATAU SALAH NAMA)
class PengaduanSerializer(serializers.ModelSerializer):
    # Menampilkan nama pelapor, bukan hanya ID-nya (praktik terbaik)
    pelapor_nama = serializers.CharField(source='pelapor.nama_lengkap', read_only=True)
    
    class Meta:
        model = Pengaduan
        fields = ['id', 'judul', 'deskripsi', 'status', 'tanggal_lapor', 'pelapor', 'pelapor_nama']
        read_only_fields = ['status', 'tanggal_lapor']