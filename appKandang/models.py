from django.db import models

class KandangAyam(models.Model):
    nama_kandang = models.CharField(max_length=100)
    kapasitas = models.IntegerField()

    def __str__(self):
        return self.nama_kandang
    
    def jumlah_ayam(self):
        return self.ayam.count()


class Ayam(models.Model):
    jenis = models.CharField(max_length=50, choices=[('petelur', 'Petelur'), ('pedaging', 'Pedaging')])
    usia = models.IntegerField()
    kandang = models.ForeignKey(
        KandangAyam,
        on_delete=models.CASCADE,
        related_name="ayam"
    )

    def __str__(self):
        return self.jenis