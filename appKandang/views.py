from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import KandangAyam
from .models import Ayam


def index(request):
    kandang_list = KandangAyam.objects.all()

    for kandang in kandang_list:
        kandang.is_penuh = kandang.ayam.count() >= kandang.kapasitas
    return render(request, 'index.html', {'kandang_list': kandang_list})

def tambah_edit_kandang(request, kandang_id=None):
    if kandang_id:
        kandang = get_object_or_404(KandangAyam, id=kandang_id)
    else:
        kandang = None

    if request.method == 'POST':
        nama_kandang = request.POST.get('nama-kandang')
        kapasitas = request.POST.get('kapasitas')

        if kandang:
            kandang.nama_kandang = nama_kandang
            kandang.kapasitas = kapasitas
            kandang.save()
        else:
            kandang = KandangAyam(nama_kandang=nama_kandang, kapasitas=kapasitas)
            kandang.save()

        return redirect('index')

    kandang_list = KandangAyam.objects.all()
    return render(request, 'index.html', {'kandang': kandang, 'kandang_list': kandang_list})

def tambah_ayam(request):
    if request.method == 'POST':
        jenis_ayam = request.POST.get('jenisAyam')
        usia = request.POST.get('usia')
        kandang_id = request.POST.get('kandangAyam')

        kandang = KandangAyam.objects.get(id=kandang_id)
        ayam = Ayam(jenis=jenis_ayam, usia=usia, kandang=kandang)
        ayam.save()

        return redirect('index')
    
    kandang_list = KandangAyam.objects.all()
    return render(request, 'index.html', {'kandang_list': kandang_list})

def hapus_kandang(request, kandang_id):
    if request.method == 'POST':
        kandang = get_object_or_404(KandangAyam, id=kandang_id)

        kandang.delete()

        return redirect('index')