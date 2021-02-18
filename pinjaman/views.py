from django.shortcuts import render

def pinjaman(request):
    return render(request, 'pinjaman/index.html')
