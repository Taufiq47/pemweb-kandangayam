from django.contrib import admin

# Register your models here.
from .models import KandangAyam
from .models import Ayam

admin.site.register(KandangAyam)
admin.site.register(Ayam)