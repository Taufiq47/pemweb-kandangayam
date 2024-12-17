from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('tambah-kandang/', views.tambah_edit_kandang, name='tambah_kandang'),
    path('tambah-ayam/', views.tambah_ayam, name='tambah_ayam'),
    path('detail-kandang/<int:kandang_id>', views.detail_kandang, name='detail_kandang'),
    path('edit-kandang/<int:kandang_id>/', views.tambah_edit_kandang, name='edit_kandang'),
    path('hapus-kandang/<int:kandang_id>/', views.hapus_kandang, name='hapus_kandang'),
    path('hapus-ayam/<int:ayam_id>/', views.hapus_ayam, name='hapus_ayam'),

]