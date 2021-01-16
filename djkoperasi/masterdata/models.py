from django.db import models
import datetime

saldo_choices = (
	(0,'DEBET'),
	(1,'KREDIT'),
)

laporan_choices = (
	(0,'NERACA'),
	(1,'JURNAL'),
)

status_choice=(
		(0,'Survey'),
		(1,'Anggota Baru'),
	)




class Anggota(models.Model):
	no_ba=models.CharField(max_length=255)
	nama_anggota=models.CharField(max_length=255)
	alamat=models.TextField()
	no_hp=models.CharField(max_length=13)
	nama_penjamin=models.CharField(max_length=255)
	tanggal=models.DateField(default=datetime.date.today)
	keterangan=models.TextField()
	status=models.IntegerField(choices=status_choice)

	def __str__(self):
		return self.nama_anggota

# Class Akun / COA

class Akun(models.Model):
    kodeakun = models.CharField(max_length=20,verbose_name='Kode*')
    namaakun = models.CharField(max_length=50,verbose_name='Nama*')
    tabelbantuan = models.CharField(max_length=20,verbose_name='Tabel Bantuan*')
    possaldo = models.IntegerField(choices=saldo_choices,verbose_name='Pos Saldo*')
    poslaporan = models.IntegerField(choices=laporan_choices,verbose_name='Pos Laporan*')
    saldoawal = models.CharField(max_length=50,verbose_name='Saldo Awal*')
    aktif = models.BooleanField(verbose_name='Aktif*')

    def __str__(self):
    	return self.kodeakun