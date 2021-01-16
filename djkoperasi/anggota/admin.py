from django.contrib import admin

# Register your models here.
from .models import Anggota



class AnggotaAdmin (admin.ModelAdmin):
    list_display = ('no_ba','nama_anggota','alamat','no_hp','nama_penjamin','tanggal','keterangan','status')

admin.site.register(Anggota, AnggotaAdmin)