from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import KandangAyam
from .models import Ayam


def index(request):
    kandang_list = KandangAyam.objects.all()

    for kandang in kandang_list:
        kandang.is_penuh = kandang.ayam.count() >= kandang.kapasitas
    return render(request, 'index.html', {'kandang_list': kandang_list})

def detail_kandang(request, kandang_id):
    kandang = get_object_or_404(KandangAyam, id=kandang_id)
    list_ayam = Ayam.objects.filter(kandang=kandang)

    jenis = request.GET.get('jenis')
    if jenis:
        list_ayam = list_ayam.filter(jenis=jenis)

    usia_min = request.GET.get('usia_min')
    usia_max = request.GET.get('usia_max')

    if usia_min:
        list_ayam = list_ayam.filter(usia__gte=int(usia_min))
    if usia_max:
        list_ayam = list_ayam.filter(usia__lte=int(usia_max))

    return render(request, 'pages/daftarAyam.html', {'list_ayam': list_ayam, 'kandang': kandang})

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
        
        messages.success(request, "Kandang ayam berhasil ditambahkan")
        return redirect('index')

    kandang_list = KandangAyam.objects.all()
    return render(request, 'index.html', {'kandang': kandang, 'kandang_list': kandang_list})

def tambah_ayam(request):
    if request.method == 'POST':
        jenis_ayam = request.POST.get('jenisAyam')
        usia = request.POST.get('usia')
        kandang_id = request.POST.get('kandangAyam')
        jumlah = int(request.POST.get('jumlah', 1))

        kandang = KandangAyam.objects.get(id=kandang_id)
        for _ in range(jumlah):
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

def hapus_ayam(request, ayam_id):
    ayam = get_object_or_404(Ayam, id=ayam_id)
    kandang_id = ayam.kandang.id
    ayam.delete()
    return redirect('detail_kandang', kandang_id=kandang_id)