# warga/models.py
from django.db import models
from django.urls import reverse # Diperlukan untuk get_absolute_url

class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True, verbose_name="Nomor Induk Kependudukan")
    nama_lengkap = models.CharField(max_length=100, verbose_name="Nama Lengkap")
    alamat = models.TextField(verbose_name="Alamat Tinggal")
    no_telepon = models.CharField(max_length=15, blank=True, verbose_name="Nomor Telepon")
    tanggal_registrasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_lengkap
    
    # Memastikan redirect berhasil setelah Create/Update
    def get_absolute_url(self):
        return reverse('warga-detail', kwargs={'pk': self.pk})

class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]
    
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BARU')
    tanggal_lapor = models.DateTimeField(auto_now_add=True)
    
    # ForeignKey: Menghubungkan ke Warga (sisi "satu")
    pelapor = models.ForeignKey(Warga, on_delete=models.CASCADE, related_name='pengaduan')

    def __str__(self):
        return self.judul
    
    def get_absolute_url(self):
        # Arahkan ke daftar pengaduan setelah aksi
        return reverse('pengaduan-list')
