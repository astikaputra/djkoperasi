from django.contrib import admin

# Register your models here.

from .models import Anggota,Akun

class AnggotaAdmin (admin.ModelAdmin):
    list_display = ('no_ba','nama_anggota','alamat','no_hp','nama_penjamin','tanggal','keterangan','status')
admin.site.register(Anggota, AnggotaAdmin)

#@admin.register(Akun)
class AkunAdmin (admin.ModelAdmin):
    list_display = ('kodeakun','namaakun','tabelbantuan','poslaporan','saldoawal','aktif')
#    list_filter = ('kodeakun','namaakun')
#	search_fields = ['namaakun']
#	list_per_page = 25

admin.site.register(Akun, AkunAdmin)