
from django.contrib import admin
from django.urls import path, re_path
#from django.views.generic import TemplateView
#from accounts import views as account_views
#from django.contrib.auth import views as auth_views
#from accounts import views
from django.contrib.auth.views import LoginView
#from .vie import pinjaman
from .views import *

from .views import (
    home,
    about,
    contact
    )

urlpatterns = [
    path('home/', home, name='home'),
    re_path(r'^pages?/$', about),
   # re_path(r'^pages?/$', about),
    path('contact', contact),
    path('admin/', admin.site.urls),
    #url(r'^$', TemplateView.as_view(template_name=)'template/index.html')),
    #path('register/', account_views.Register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

   # path('', home, name='home'),
       # # url home kita
    #path('', views.home, name='home'),

    # url account
   #path('', include('accounts.urls'))
    # URL Pinjaman & tabungan
   path('pinjaman/', pinjaman.views.index(), name='pinjaman'),
  # path('tabungan/', include('tabungan.urls'), name='tabungan'),
]
