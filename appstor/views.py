from django.http import HttpResponse
from django.shortcuts import render, redirect
from .filters import SantriFilter, UstadFilter, SetorFilter
from .models import *
from .forms import SantriForm, Setorank, AsatidzForm, RegisterForm, KetForm
from django.core.paginator import Paginator
from django.contrib import messages
from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .resource import ekporResource
from django.conf import settings



# Create your views here.

def ekpos(request):
    person_resource = ekporResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'

    wb = xls.workbook(encoding='utf-8')
    ws = wb.add_sheet('Ket')

    row_num = 0
    wb.save(response)
    return response



@login_required(login_url='login') 
@ijinkan_pengguna(yang_diizinkan=['ustad'])
def profil(request):
 datacustumer = request.user.asatidz
 form = AsatidzForm(instance = datacustumer)
 if request.method == 'POST':
    form = AsatidzForm(request.POST, request.FILES, instance=datacustumer)
    if form.is_valid:
        form.save() 
   
 context = {
    'menu': 'profil',
    'formcustumer': form
 }
 return render(request, 'log/profil.html', context)



@login_required(login_url='login') 
@ijinkan_pengguna(yang_diizinkan=['ustad'])
def userPage(request):
    a = Asatidz.objects.all()
    order_custumer = request.user.asatidz.setoran_set.all()
    
 # tampil
    a = Asatidz.objects.all()
    detailust = a.filter(marhalah='Tamhidiyah')
    bk = a.filter(marhalah='Idadiyah')
    ck = a.filter(marhalah='Mahad Aly')
# pndah halaman
    halaman_tampil = Paginator(detailust, 2)
    halaman_url = request.GET.get('halaman',1)
    halaman_order = halaman_tampil.get_page(halaman_url)

    if halaman_order.has_previous():
         url_previous = f'?halaman={halaman_order.previous_page_number()}'
    else:
         url_previous = ''
    if halaman_order.has_next():
         url_next = f'?halaman={halaman_order.next_page_number()}'
    else:
         url_next = ''

    halaman_tampil2 = Paginator(bk, 2)
    halaman_url2 = request.GET.get('halaman',1)
    halaman_order2 = halaman_tampil2.get_page(halaman_url2)

    if halaman_order2.has_previous():
         url_previous2 = f'?halaman={halaman_order2.previous_page_number()}'
    else:
         url_previous2 = ''
    if halaman_order2.has_next():
         url_next2 = f'?halaman={halaman_order2.next_page_number()}'
    else:
         url_next2 = ''

    halaman_tampil3 = Paginator(ck, 2)
    halaman_url3 = request.GET.get('halaman',1)
    halaman_order3 = halaman_tampil3.get_page(halaman_url3)

    if halaman_order3.has_previous():
         url_previous3 = f'?halaman={halaman_order3.previous_page_number()}'
    else:
         url_previous3 = ''
    if halaman_order3.has_next():
         url_next3 = f'?halaman={halaman_order3.next_page_number()}'
    else:
         url_next3 = ''
# nilai angka
    list_muin = Santri.objects.all()
    filters = list_muin.count()
    filterp = list_muin.filter(jk ='perempuan').count()
    filterl = list_muin.filter(jk ='laki-laki').count()
#   jumlah 
    filterlt = list_muin.filter(jk ='laki-laki')
    filterlpr = list_muin.filter(jk ='perempuan')
#  tamhid
    tmp = filterlpr.filter(marhalah = 'Tamhidiyah').count()
    tm = filterlt.filter(marhalah = 'Tamhidiyah').count()

# idad
    il = filterlt.filter(marhalah = 'Idadiyah').count()
    ip = filterlpr.filter(marhalah = 'Idadiyah').count()
# mahad aly
    mal = filterlt.filter(marhalah = 'Mahad Aly').count()
    map = filterlpr.filter(marhalah = 'Mahad Aly').count()
# nilai marhalah
    
    filtert = list_muin.filter(marhalah ='Tamhidiyah').count()
    filteri = list_muin.filter(marhalah ='Idadiyah').count()
    filterm = list_muin.filter(marhalah ='Mahad Aly').count()
# aksi 
    context = {
        
        'judul' : 'Beranda',
        'menu': '',
        'page': 'beranda',
        'sn': filters,
        'tm': filtert,
        'id': filteri,
        'ma': filterm,
        'l': filterl,
        'p': filterp,

        't': tm,
        'tp':tmp,
       
        'idl': il,
        'idp': ip,

        'mal': mal,
        'map': map,

# page ustad
        'data_order_custumer':order_custumer,   
        'halaman_order_custumer':halaman_order,
        'previous' : url_previous,
        'next' : url_next,
        'halaman_order_custumer2':halaman_order2,
        'previous2' : url_previous2,
        'next2' : url_next2,
        'halaman_order_custumer3':halaman_order3,
        'previous' : url_previous3,
        'next' : url_next3,
    }
    return render(request, 'log/user.html', context)

@tolakhalaman_ini
def loginPage (request):
#   if request.user.is_authenticated:
#     return redirect('home')
#   else:
        formlogin = AuthenticationForm
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            cocokan = authenticate(request, username=username, password=password )
            if cocokan is not None:
                login(request, cocokan)
                return redirect('home')

        context = {
            'judul': 'Halaman Login',
            'menu': 'login',
            'tampillogin' : formlogin
            }
        return render(request, 'log/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@tolakhalaman_ini
def registerPage (request):
#  if request.user.is_authenticated:
#      return redirect('home')
#  else:
    formregister = RegisterForm() 
    if request.method == 'POST':
        formregister = RegisterForm(request.POST)
        if formregister.is_valid():
            nilaiusername = formregister.cleaned_data.get('username')
            messages.success(request, f'Username Anda adalah {nilaiusername}')
            group_custumer = formregister.save()
            grup = Group.objects.get(name='ustad')
            group_custumer.groups.add(grup)
            Asatidz.objects.create(
                  user=group_custumer,
                  nama=group_custumer.username)

            return redirect('login')
    context = {
        'judul': 'Halaman Register',
        'menu': 'register',
        'tampilregister' : formregister
        }
    return render(request, 'log/register.html', context)

 

@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
@pilihan_login
def home(request):
# tampil
    a = Asatidz.objects.all()
    detailust = a.filter(marhalah='Tamhidiyah')
    bk = a.filter(marhalah='Idadiyah')
    ck = a.filter(marhalah='Mahad Aly')
# pndah halaman
    halaman_tampil = Paginator(detailust, 2)
    halaman_url = request.GET.get('halaman',1)
    halaman_order = halaman_tampil.get_page(halaman_url)

    if halaman_order.has_previous():
         url_previous = f'?halaman={halaman_order.previous_page_number()}'
    else:
         url_previous = ''
    if halaman_order.has_next():
         url_next = f'?halaman={halaman_order.next_page_number()}'
    else:
         url_next = ''

    halaman_tampil2 = Paginator(bk, 2)
    halaman_url2 = request.GET.get('halaman',1)
    halaman_order2 = halaman_tampil2.get_page(halaman_url2)

    if halaman_order2.has_previous():
         url_previous2 = f'?halaman={halaman_order2.previous_page_number()}'
    else:
         url_previous2 = ''
    if halaman_order2.has_next():
         url_next2 = f'?halaman={halaman_order2.next_page_number()}'
    else:
         url_next2 = ''

    halaman_tampil3 = Paginator(ck, 2)
    halaman_url3 = request.GET.get('halaman',1)
    halaman_order3 = halaman_tampil3.get_page(halaman_url3)

    if halaman_order3.has_previous():
         url_previous3 = f'?halaman={halaman_order3.previous_page_number()}'
    else:
         url_previous3 = ''
    if halaman_order3.has_next():
         url_next3 = f'?halaman={halaman_order3.next_page_number()}'
    else:
         url_next3 = ''
# nilai angka
    list_muin = Santri.objects.all()
    filters = list_muin.count()
    filterp = list_muin.filter(jk ='perempuan').count()
    filterl = list_muin.filter(jk ='laki-laki').count()
#   jumlah 
    filterlt = list_muin.filter(jk ='laki-laki')
    filterlpr = list_muin.filter(jk ='perempuan')
#  tamhid
    tmp = filterlpr.filter(marhalah = 'Tamhidiyah').count()
    tm = filterlt.filter(marhalah = 'Tamhidiyah').count()

# idad
    il = filterlt.filter(marhalah = 'Idadiyah').count()
    ip = filterlpr.filter(marhalah = 'Idadiyah').count()
# mahad aly
    mal = filterlt.filter(marhalah = 'Mahad Aly').count()
    map = filterlpr.filter(marhalah = 'Mahad Aly').count()


  

# nilai marhalah
    
    filtert = list_muin.filter(marhalah ='Tamhidiyah').count()
    filteri = list_muin.filter(marhalah ='Idadiyah').count()
    filterm = list_muin.filter(marhalah ='Mahad Aly').count()
# aksi 
    context = {
        
        'judul' : 'Beranda',
        'menu': '',
        'page': 'beranda',
        'sn': filters,
        'tm': filtert,
        'id': filteri,
        'ma': filterm,
        'l': filterl,
        'p': filterp,

        't': tm,
        'tp':tmp,
       
        'idl': il,
        'idp': ip,

        'mal': mal,
        'map': map,

# page ustad
        'halaman_order_custumer':halaman_order,
        'previous' : url_previous,
        'next' : url_next,
        'halaman_order_custumer2':halaman_order2,
        'previous2' : url_previous2,
        'next2' : url_next2,
        'halaman_order_custumer3':halaman_order3,
        'previous' : url_previous3,
        'next' : url_next3,
    }
    return render(request, 'data/dashboard.html', context)


# tampil asatidz
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def setorasatidz(request,wd):
    s = Asatidz.objects.get(id=wd)
    mbahss = s.setoran_set.all()
    filter_santrim = UstadFilter(request.GET, queryset=mbahss)
    mbahss =filter_santrim.qs
    
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Idadiyah',
        'menu': 'muin',
        'page': 'idadiyah',  
        'datasetorsantria': mbahss,
        'filter_data_ustadz': filter_santrim,
    }
    return render(request, 'crud/viewustad.html', context)

@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
def idad(request):

    context = {
        'judul' : 'Marhalah Idadiyah',
        'menu': 'idad',
        'page': 'idadiyah',        
    }
    return render(request, 'data/idadiyah.html', context)

@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
def faroid(request):
    list_muin = Santri.objects.all()
    filtermin = list_muin.filter(takhossus ='faroid')
    filter_santrim = SantriFilter(request.GET, queryset=filtermin)
    filtermin =filter_santrim.qs
    context = {
        'judul' : 'Marhalah Idadiyah',
        'menu': 'faroid',
        'page': 'idadiyah', 
        'faroid': filtermin,       
        
        'filter_data_santri': filter_santrim,

     }
    return render(request, 'data/faroid.html', context)
@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
def muin(request):
    list_muin = Santri.objects.all()
    filterminm = list_muin.filter(takhossus ='fathul muin')
    filter_santrim = SantriFilter(request.GET, queryset=filterminm)
    filterminm =filter_santrim.qs
    context = {
        'judul' : 'Marhalah Idadiyah',
        'menu': 'muin',
        'page': 'idadiyah',      
        'muin': filterminm,     
        'filter_data_santri': filter_santrim,
     }
    return render(request, 'data/Fmuin.html', context)



@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
def tamhid(request):
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'menu': 'tamhid',
        'page': 'tamhidiyah',
    }
    return render(request, 'data/tamhidiyah.html', context)

@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
def nubzah(request):
    list_qorib = Santri.objects.all()
    filterqrbn = list_qorib.filter(takhossus = 'nubzah')
    filter_santrin = SantriFilter(request.GET, queryset=filterqrbn)
    filterqrbn =filter_santrin.qs
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'menu': 'nubzah',
        'page': 'nubzah',
        'nubzah': filterqrbn,   
        'filter_data_santri': filter_santrin,
    }
    return render(request, 'data/nubzah.html', context)

@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
def qorib(request):
    
    list_qorib = Santri.objects.all()
    filterqrb = list_qorib.filter(takhossus ='fathul qorib')
    filter_santriq = SantriFilter(request.GET, queryset=filterqrb)
    filterqrb =filter_santriq.qs
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'menu': 'qorib',
        'page': 'qorib',
        'qorib': filterqrb,   
        'filter_data_santri': filter_santriq,
    }
    return render(request, 'data/Fqorib.html', context)


# buat setoran baru
@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
def tbsetor(request):
    tmbahss = Setorank()
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')
    context = {
        'judul' : 'santri',
        'menu': 'tbsntr',
        'page': 'form santri',
        'form' : tmbahss, 
    }
    return render(request, 'setoranbaru/brnubzah.html', context)


# tambah setoran
@login_required(login_url='login')
def setorqrb(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/qorib')
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'form': m,
    }
    return render(request, 'data/strqorib.html', context)
def editqrb(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST, instance=s)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/qorib')
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'form': m,
    }
    return render(request, 'data/editmuin.html', context)

@login_required(login_url='login')
def setornbz(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/nubzah')
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'form': m,
    }
    return render(request, 'data/strnubzah.html', context)
def editnbz(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST, instance=s)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/nubzah')
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'form': m,
    }
    return render(request, 'data/editmuin.html', context)

@login_required(login_url='login')
def setormuin(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/muin')
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'form': m,
    }
    return render(request, 'data/strmuin.html', context)
def editmuin(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST, instance=s)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/muin')
    context = {
        'judul' : 'Marhalah Idadiyah',
        'form': m,
    }
    return render(request, 'data/editmuin.html', context)

@login_required(login_url='login')
def setorfaroid(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/faroid')
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'form': m,
    }
    return render(request, 'data/strfaroid.html', context)

def editfaroid(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST, instance=s)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/faroid')
    context = {
        'judul' : 'Marhalah Idadiyah',
        'form': m,
    }
    return render(request, 'data/editmuin.html', context)

@login_required(login_url='login')
def setorusul(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/usul')
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'form': m,
    }
    return render(request, 'data/strusul.html', context)
def editusul(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST, instance=s)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/usul')
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'form': m,
    }
    return render(request, 'data/editmuin.html', context)

@login_required(login_url='login')
def setorqowaid(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/qowaid')
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'form': m,
    }
    return render(request, 'data/strqowaid.html', context)
def editqowaid(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST, instance=s)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/muin')
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'form': m,
    }
    return render(request, 'data/editmuin.html', context)

@login_required(login_url='login')
def setormantiq(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/mantiq')
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'form': m,
    }
    return render(request, 'data/strmantiq.html', context)
def editmantiq(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST, instance=s)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/mantiq')
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'form': m,
    }
    return render(request, 'data/editmuin.html', context)

@login_required(login_url='login')
def setorbalaghoh(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/balagoh')
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'form': m,
    }
    return render(request, 'data/strbalaghoh.html', context)
def editbalaghoh(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST, instance=s)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/balagoh')
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'form': m,
    }
    return render(request, 'data/editmuin.html', context)

@login_required(login_url='login')
def setorarudl(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/arudl')
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        'form': m,
    }
    return render(request, 'data/strarudl.html', context)
def editarudl(request,e):
    s = Setoran.objects.get(id=e)
    m = Setorank(instance=s)
    if request.method == 'POST':
        formsimpan = Setorank(request.POST, instance=s)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/arudl')
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'form': m,
    }
    return render(request, 'data/editmuin.html', context)
@login_required(login_url='login')



# @ijinkan_pengguna(yang_diizinkan=['admin'])

# tampil data ustad dan ket santri
def setorasatidz(request,wd):
    s = Asatidz.objects.get(id=wd)
    mbahss = s.setoran_set.all()
  
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Asatidz',
        'menu': 'pengajar',
        'page': '',  
        'datasetorsantria': mbahss,
    }
    return render(request, 'crud/viewustad.html', context)

def tampilket(request,wd):
    s = Santri.objects.get(id=wd)
    mbahss = s.ket_set.all()
  
    if request.method == 'POST':
        formsimpan = KetForm(request.POST)
    context = {
        'judul' : 'Asatidz',
        'menu': 'pengajar',
        'page': '',  
        'ket': mbahss,
    }
    return render(request, 'crud/viewket.html', context)

# tampil setoran
@login_required(login_url='login')
def strmuin(request,wd):
    s = Santri.objects.get(id=wd)
    mbahss = s.setoran_set.all()
    j = mbahss.filter(takhossus ='4')
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Idadiyah',
        'menu': 'muin',
        'page': 'idadiyah',  
        'datasetorsantria': j,
    }
    return render(request, 'crud/viewmuin.html', context)


@login_required(login_url='login')
def strfaroid(request,wd):
    s = Santri.objects.get(id=wd)
    mbahss = s.setoran_set.all()
    j = mbahss.filter(takhossus ='5')
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Idadiyah',
        'menu': 'faroid',
        'page': 'idadiyah',        
        'datasetorsantria': j,
    }
    return render(request, 'crud/viewfaroid.html', context)

@login_required(login_url='login')
def strnubzah(request, wd):
    s = Santri.objects.get(id=wd)
    mbahss = s.setoran_set.all()
    j = mbahss.filter(takhossus ='2')
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        # 'form': mbahss,
        'datasetorsantria': j,
    }
    return render(request, 'crud/viewnubzah.html', context)

@login_required(login_url='login')
def strqorib(request,w):
    s = Santri.objects.get(id=w)
    mbahss = s.setoran_set.all()
    j = mbahss.filter(takhossus ='3')
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Tamhidiyah',
        # 'form': mbahss,
        'datasetorsantri': j,
    }
    return render(request, 'crud/viewfq.html', context)

@login_required(login_url='login')
def strusul(request,wd):
    s = Santri.objects.get(id=wd)
    mbahss = s.setoran_set.all()
    j = mbahss.filter(takhossus ='10')
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'strusul',
        'page': 'usul fiqh',
        'datasetorsantria': j,
    }
    return render(request, 'crud/viewusul.html', context)

@login_required(login_url='login')
def strmantiq(request,wd):
    s = Santri.objects.get(id=wd)
    mbahss = s.setoran_set.all()
    j = mbahss.filter(takhossus ='6')
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'strmantiq',
        'page': 'mantiq',
        'datasetorsantria': j,
    }
    return render(request, 'crud/viewmantiq.html', context)

@login_required(login_url='login')
def strarudl(request,wd):
    s = Santri.objects.get(id=wd)
    mbahss = s.setoran_set.all()
    j = mbahss.filter(takhossus ='8')
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'strarudl',
        'page': 'arudl',
        'datasetorsantria': j,
    }
    return render(request, 'crud/viewarudl.html', context)
def strqowaid(request,wd):
    s = Santri.objects.get(id=wd)
    mbahss = s.setoran_set.all()
    j = mbahss.filter(takhossus ='9')
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'strqowaid',
        'page': 'qowaid fiqh',
        'datasetorsantria': j,
    }
    return render(request, 'crud/viewqowaid.html', context)
def strbalaghoh(request,wd):
    s = Santri.objects.get(id=wd)
    mbahss = s.setoran_set.all()
    j = mbahss.filter(takhossus ='7')
    if request.method == 'POST':
        formsimpan = Setorank(request.POST)
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'strbalagoh',
        'page': 'balaghoh',
        'datasetorsantria': j,
    }
    return render(request, 'crud/viewbalaghoh.html', context)




# ma'had aly


@login_required(login_url='login')
def mahad(request):
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'alyy',
        'page': 'mahad aly',
    }
    return render(request, 'data/mahadaly.html', context)

@login_required(login_url='login')
def usul(request):
    list_usul = Santri.objects.all()
    filterusul = list_usul.filter(takhossus ='usul fiqh')
    filter_santri = SantriFilter(request.GET, queryset=filterusul)
    filterusul =filter_santri.qs
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'usul',
        'page': 'usul fiqh',
        'usul': filterusul,
        'filter_data_santri': filter_santri,
    }
    return render(request, 'data/usulfiqh.html', context)

@login_required(login_url='login')
def mantiq(request):
    list_mtq = Santri.objects.all()
    filtermtq = list_mtq.filter(takhossus ='mantiq')
    filter_santri = SantriFilter(request.GET, queryset=filtermtq)
    filtermtq =filter_santri.qs
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'mantiq',
        'page': 'mantiq',
        'mantiq' : filtermtq,
        'filter_data_santri': filter_santri,
    }
    return render(request, 'data/mantiq.html', context)

@login_required(login_url='login')
def arudl(request):
    list_arudl = Santri.objects.all()
    filterarudl = list_arudl.filter(takhossus ='arudl')
    filter_santri = SantriFilter(request.GET, queryset=filterarudl)
    filterarudl =filter_santri.qs
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'arudl',
        'page': 'arudl',
        'arudl': filterarudl,
        'filter_data_santri': filter_santri,
    }
    return render(request, 'data/arudl.html', context)

@login_required(login_url='login')
def qowaid(request):
    list_qwd = Santri.objects.all()
    filterqwd = list_qwd.filter(takhossus ='qowaid fiqh')
    filter_santri = SantriFilter(request.GET, queryset=filterqwd)
    filterqwd =filter_santri.qs
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'qowaid',
        'page': 'qowaid fiqh',
        'qowaid' : filterqwd,
        'filter_data_santri': filter_santri,
    }
    return render(request, 'data/qowaidfiqh.html', context)

@login_required(login_url='login')
def balaghoh(request):
    list_blg = Santri.objects.all()
    filterblg = list_blg.filter(takhossus ='balaghoh')
    filter_santri = SantriFilter(request.GET, queryset=filterblg)
    filterblg =filter_santri.qs
    context = {
        'judul' : 'Marhalah Mahad Aly',
        'menu': 'balagoh',
        'page': 'balaghoh',
        'balaghoh': filterblg,
        'filter_data_santri': filter_santri,
    }
    return render(request, 'data/balaghoh.html', context)

# Asatidz
@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
def asatidz(request):
    list_sn = Asatidz.objects.order_by('nama')
    filter_ustad = UstadFilter(request.GET, queryset=list_sn)
    list_sn =filter_ustad.qs
#  jumlah
    filters = list_sn.count()
    filterp = list_sn.filter(jk ='perempuan').count()
    filterl = list_sn.filter(jk ='laki-laki').count()

    filtert = list_sn.filter(marhalah ='Tamhidiyah').count()
    filteri = list_sn.filter(marhalah ='Idadiyah').count()
    filterm = list_sn.filter(marhalah ='Mahad Aly').count()


 # pagination
    halaman_tampil = Paginator(list_sn, 6)
    halaman_url = request.GET.get('halaman',1)
    halaman_order = halaman_tampil.get_page(halaman_url)

    if halaman_order.has_previous():
         url_previous = f'?halaman={halaman_order.previous_page_number()}'
    else:
         url_previous = ''
    if halaman_order.has_next():
         url_next = f'?halaman={halaman_order.next_page_number()}'
    else:
         url_next = ''
    context = {
        'judul' : 'asatidz mahad aly',
        'menu': 'asatidz',
        'page': 'asatidz',
  # 'js' : list_sn,
        'filter_data_ustad': filter_ustad,

        'halaman_order_custumer':halaman_order,
        'previous' : url_previous,
        'next' : url_next,
  #  jumlh
        'sn': filters,
        'tm': filtert,
        'id': filteri,
        'ma': filterm,
        'l': filterl,
        'p': filterp,
    }
    return render(request, 'data/asatidz.html', context)
#crud
def tbasatidz(request):
    tmbahss = AsatidzForm()
    if request.method == 'POST':
        formsimpan = AsatidzForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/asatidz')
    context = {
        'judul' : 'asatidz',
        'menu': 'tbasatidz',
        'page': 'form asatidz',
        'form' : tmbahss, 
    }
    return render(request, 'crud/tambahasatidz.html', context)
    
def upasatidz(request,p):
    ups = Asatidz.objects.get(id=p)
    formsan = AsatidzForm(instance=ups)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = AsatidzForm(request.POST, instance=ups)
        if formedit.is_valid:
            formedit.save()
            return redirect('/asatidz')
    context = {
         'judul' : 'asatidz',
         'form' : formsan, 
        }
    return render(request, 'crud/tambahasatidz.html', context)
def hpsasatidz(request, pk):
    pussan = Asatidz.objects.get(id=pk)
    if request.method == 'POST':
        pussan.delete()
        return redirect('/asatidz')

    context = {
        'judul': 'Hapus Data ',
        'hapussantri' : pussan, 
        }
    return render(request, 'crud/fhapus.html', context)

# satntri
@ijinkan_pengguna(yang_diizinkan=['admin'])
def santri(request):
    list_sn = Santri.objects.order_by('nama')
    a = Santri.objects.all()
    filter_santri = SantriFilter(request.GET, queryset=list_sn)
    list_sn =filter_santri.qs
# jumlah
    filters = a.count()
    filterp = a.filter(jk ='perempuan').count()
    filterl = a.filter(jk ='laki-laki').count()

    filtert = a.filter(marhalah ='Tamhidiyah').count()
    filteri = a.filter(marhalah ='Idadiyah').count()
    filterm = a.filter(marhalah ='Mahad Aly').count()
# pagination
    halaman_tampil = Paginator(list_sn, 8)
    halaman_url = request.GET.get('halaman',1)
    halaman_order = halaman_tampil.get_page(halaman_url)

    if halaman_order.has_previous():
         url_previous = f'?halaman={halaman_order.previous_page_number()}'
    else:
         url_previous = ''
    if halaman_order.has_next():
         url_next = f'?halaman={halaman_order.next_page_number()}'
    else:
         url_next = ''

    context = {
 # isi
        'judul' : 'santri',
        'menu': 'sntr',
        'page': 'santri',
# 'js' : list_sn,
        'filter_data_santri': filter_santri,
        
        'halaman_order_custumer':halaman_order,
        'previous' : url_previous,
        'next' : url_next,
# jumlah
        'sn': filters,
        'tm': filtert,
        'id': filteri,
        'ma': filterm,
        'l': filterl,
        'p': filterp,

    }
    return render(request, 'data/santri.html', context)
#crud
def tbsantri(request):
    tmbahss = SantriForm()
    if request.method == 'POST':
        formsimpan = SantriForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/santri')
    context = {
        'judul' : 'santri',
        'menu': 'tbsntr',
        'page': 'form santri',
        'form' : tmbahss, 
    }
    return render(request, 'crud/tambahsntr.html', context)
    
def upsantri(request,p):
    ups = Santri.objects.get(id=p)
    formsan = SantriForm(instance=ups)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = SantriForm(request.POST, instance=ups)
        if formedit.is_valid:
            formedit.save()
            return redirect('/santri')
    context = {
         'judul' : 'santri',
         'form' : formsan, 
        }
    return render(request, 'crud/tambahsntr.html', context)

def hpssantri(request, pk):
    pussan = Santri.objects.get(id=pk)
    if request.method == 'POST':
        pussan.delete()
        return redirect('/santri')

    context = {
        'judul': 'Hapus Data Order',
        'hapussantri' : pussan, 
        }
    return render(request, 'crud/fhapus.html', context)



def hpssetoran(request, pk):
    pussan = Setoran.objects.get(id=pk)
    if request.method == 'POST':
        pussan.delete()
        return redirect('/')

    context = {
        'judul': 'Hapus Data Order',
        'hapussantri' : pussan, 
        }
    return render(request, 'crud/fhapus.html', context)


def ketsantri(request):
    list_sn = Ket.objects.order_by('takhossus')
    a = Ket.objects.all()
    context = {
        'judul': 'keterangan santri',
        
        'menu': 'ket',
        'page': 'keterangan',
        'ket' : a, 
        }
   
    return render(request, 'data/ket.html', context)
def tbket(request):
    tmbahss = KetForm()
    if request.method == 'POST':
        formsimpan = KetForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/ketsantri')
    context = {
        'judul' : 'ket',
        'menu': 'ket',
        'page': 'keterangan',
        'form' : tmbahss, 
    }
    return render(request, 'crud/tambahketsntr.html', context)
    
def upket(request,p):
    ups = Ket.objects.get(id=p)
    formsan = KetForm(instance=ups)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = KetForm(request.POST, instance=ups)
        if formedit.is_valid:
            formedit.save()
            return redirect('/ketsantri')
    context = {
         'judul' : 'keterangan santri',
         'menu' : 'ket',
         'form' : formsan, 
        }
    return render(request, 'crud/tambahketsntr.html', context)

def hpsket(request, pk):
    pussan = Ket.objects.get(id=pk)
    if request.method == 'POST':
        pussan.delete()
        return redirect('/ketsantri')

    context = {
        'judul': 'Hapus Data Order',
        'hapussantri' : pussan, 
        }
    return render(request, 'crud/fhapus.html', context)

#crud