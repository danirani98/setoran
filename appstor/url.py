from django.urls import path
from . import views
from django.conf import settings
from .forms import *
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('tamhid/', views.tamhid, name='tamhid'),
    path('nubzah/', views.nubzah, name='nubzah'),

# login & register
    path('user/', views.userPage, name='user-page'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),


 


# tampil setoran
    path('strnubzah/<str:wd>', views.strnubzah, name='strnubzah'),
    path('strqorib/<str:w>', views.strqorib, name='strqorib'),
    path('strmuin/<str:wd>', views.strmuin, name='strmuin'),
    path('strfaroid/<str:wd>', views.strfaroid, name='strfaroid'),
   


# copui
    path('strarudl/<str:wd>', views.strarudl, name='strarudl'),
    path('strbalaghoh/<str:wd>', views.strbalaghoh, name='strbalaghoh'),
    path('strmantiq/<str:wd>', views.strmantiq, name='strmantiq'),
    path('strqowaid/<str:wd>', views.strqowaid, name='strqowaid'),
    path('strusul/<str:wd>', views.strusul, name='strusul'),
# tampil ustad
    path('setorasatidz/<str:wd>', views.setorasatidz, name='setorasatidz'),

#tampil data keterangan
    path('tampilkets/<str:wd>', views.tampilket, name='tampilket'), 
   


# tambah setor 

    path('setorarudl/<str:e>', views.setorarudl, name='setorarudl'),
    path('setorbalaghoh/<str:e>', views.setorbalaghoh, name='setorbalaghoh'),
    path('setormantiq/<str:e>', views.setormantiq, name='setormantiq'),
    path('setorqowaid/<str:e>', views.setorqowaid, name='setorqowaid'),
    path('setorusul/<str:e>', views.setorusul, name='setorusul'),






# setoran baru
    path('setorbaru', views.tbsetor, name='setorbaru'),

# tambah setor 
    path('setornbz/<str:e>', views.setornbz, name='setornubzah'),
    path('setorqrb/<str:e>', views.setorqrb, name='setorqorib'),
    path('setormuin/<str:e>', views.setormuin, name='setormuin'),
    path('setorfaroid/<str:e>', views.setorfaroid, name='setorfaroid'),


#edit setor
    path('editarudl/<str:e>', views.editarudl, name='edit_setor3'),
    path('editbalaghoh/<str:e>', views.editbalaghoh, name='edit_setor4'),
    path('editmantiq/<str:e>', views.editmantiq, name='edit_setor5'),
    path('editqowaid/<str:e>', views.editqowaid, name='edit_setor6'),
    path('editusul/<str:e>', views.editusul, name='edit_setor7'),
    path('editnbz/<str:e>', views.editnbz, name='edit_setor2'),
    path('editqrb/<str:e>', views.editqrb, name='edit_setor1'),
    path('editrmuin/<str:e>', views.editmuin, name='editmuin'),
    path('editfaroid/<str:e>', views.editfaroid, name='edit_setor'),

# data takhossus
    path('qorib', views.qorib, name='qorib'),

    path('idad', views.idad, name='idad'),
    path('muin', views.muin, name='muin'),
    path('faroid', views.faroid, name='faroid'),
  
    path('hpssetoran/<str:pk>', views.hpssetoran, name='delete_setor'),
    # path('strfaroid', views.strfaroid, name='strfaroid'),

    path('mahadaly', views.mahad, name='aly'),
    path('usul', views.usul, name='usul'),
    path('qowaid', views.qowaid, name='qowaid'),
    path('mantiq', views.mantiq, name='mantiq'),
    path('balagoh', views.balaghoh, name='balagoh'),
    path('arudl', views.arudl, name='arudl'),


# santri
    path('santri', views.santri, name='santri'),
    path('tmbhsntr/', views.tbsantri, name='tbsantri'),
    path('upsantri/<str:p>', views.upsantri, name='update_santri'),
    path('hpssantri/<str:pk>', views.hpssantri, name='delete_santri'),

# asatidz  
    path('asatidz', views.asatidz, name='asatidz'),
    path('tmbhasatidz/', views.tbasatidz, name='tbasatidz'),
    path('upasatidz/<str:p>', views.upasatidz, name='update_asatidz'),
    path('hpsasatidz/<str:pk>', views.hpsasatidz, name='delete_asatidz'),

    path('profil/', views.profil, name='profil'),

    path('ketsantri', views.ketsantri, name='ketsantri'),
    path('tmbhketsntr/', views.tbket, name='tbketsantri'),
    path('upketsantri/<str:p>', views.upket, name='update_ketsantri'),
    path('hpsketsantri/<str:pk>', views.hpsket, name='delete_santri'),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)