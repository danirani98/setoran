# from .forms import SantriForm
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Takhossus(models.Model):
    jns={
        ('nubzah','nubzah'),
        ('fathul qorib','fathul qorib'),
        ('fathul muin','fathul muin'),
        ('faroid','faroid'),
        ('Arudl','Arudl'),
        ('mantiq','mantiq'),
        ('balaghoh','balaghoh'),
        ('qowaid','qowaid'),
        ('usul','usul'),
     }

    tkh = models.CharField(choices=jns, max_length=30, blank=True, null=True)
  
    def __str__(self):
       return self.tkh

  

class Santri(models.Model):
    jenis={
        ('laki-laki','laki-laki'),
        ('perempuan','perempuan')
     }
    statusp={
        ('siswa','siswa'),
        ('mahasiswa','mahasiswa'),
        ('salaf','salaf')
     }
    marhalah={
        ('Tamhidiyah','Tamhidiyah'),
        ('Idadiyah','Idadiyah'),
        ('Mahad Aly','Mahad Aly'),
     }
    jns={
        ('nubzah','nubzah'),
        ('fathul qorib','fathul qorib'),
        ('fathul muin','fathul muin'),
        ('faroid','faroid'),
        ('arudl','arudl'),
        ('mantiq','mantiq'),
        ('balaghoh','balaghoh'),
        ('qowaid fiqh','qowaid fiqh'),
        ('usul fiqh','usul fiqh'),
     }

   
    nama = models.CharField(max_length=200, blank=False, null=True)
    alamat = models.CharField( max_length=200, blank=True, null=True)
    # tempat_lahir = models.CharField( max_length=200, blank=True, null=True)
    # tanggal_lahir = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(choices=statusp, max_length=200, blank=True, null=True)
    jk = models.CharField(choices=jenis, max_length=20, blank=True, null=True)
    marhalah= models.CharField(choices=marhalah, max_length=30, blank=True, null=True)
    takhossus = models.CharField(choices=jns, max_length=30, blank=True, null=True)

    def __str__(self):
          return '%s' % (self.nama)
    
class Ket(models.Model):
    marhalah={
        ('Tamhidiyah','Tamhidiyah'),
        ('Idadiyah','Idadiyah'),
        ('Mahad Aly','Mahad Aly'),
     }
    ket={
        ('Lulus','Lulus'),
        ('Tidak Lulus','Tidak Lulus'),
        ('belum Lulus','belum Lulus'),
        
     }
    jns={
        ('Tamhidiyah','Tamhidiyah'),
        ('Idadiyah','Idadiyah'),
        ('Mahad Aly','Mahad Aly'),
        ('nubzah','nubzah'),
        ('fathul qorib','fathul qorib'),
        ('fathul muin','fathul muin'),
        ('faroid','faroid'),
        ('arudl','arudl'),
        ('mantiq','mantiq'),
        ('balaghoh','balaghoh'),
        ('qowaid fiqh','qowaid fiqh'),
        ('usul fiqh','usul fiqh'),
     }

   
    nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
    marhalah = models.CharField(choices=marhalah, max_length=30, blank=True, null=True)
    angkatan = models.CharField( max_length=10, blank=True, null=True)
    takhossus = models.CharField(choices=jns, max_length=200, blank=True, null=True)
    tanggal_masuk = models.DateField( max_length=200, blank=True, null=True)
    keterangan = models.CharField(choices=ket, max_length=30, blank=True, null=True)
    lulus_tanggal = models.DateField( max_length=200, blank=True, null=True)
    naik_takhossus = models.CharField(choices=jns, max_length=30, blank=True, null=True)

    def __str__(self):
          return '%s' % (self.nama)
  

class Asatidz(models.Model):
    jenis={
        ('laki-laki','laki-laki'),
        ('perempuan','perempuan')
     }
    statusp={
        ('siswa','siswa'),
        ('mahasiswa','mahasiswa'),
        ('salaf','salaf')
     }
    marhalah={
        ('Tamhidiyah','Tamhidiyah'),
        ('Idadiyah','Idadiyah'),
        ('Mahad Aly','Mahad Aly'),
     }
    jns={
        ('nubzah','nubzah'),
        ('fathul qorib','fathul qorib'),
        ('fathul muin','fathul muin'),
        ('faroid','faroid'),
        ('arudl','arudl'),
        ('mantiq','mantiq'),
        ('balaghoh','balaghoh'),
        ('qowaid fiqh','qowaid fiqh'),
        ('usul fiqh','usul fiqh'),
     }

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=False, null=True)
    alamat = models.CharField( max_length=200, blank=True, null=True)
    # tempat_lahir = models.CharField( max_length=200, blank=True, null=True)
    # tanggal_lahir = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(choices=statusp, max_length=200, blank=True, null=True)
    jk = models.CharField(choices=jenis, max_length=20, blank=True, null=True)
    marhalah= models.CharField(choices=marhalah, max_length=30, blank=True, null=True)
    profile_pic = models.ImageField(default='fotokosong.png', blank=True)


    def __str__(self):
          return '%s' % (self.nama)
    def save(self, *args, **kwargs):
        super(Asatidz, self).save( *args, **kwargs)
        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_pic.path)


          

class Setoran(models.Model):
    nilai={
        ('A','A'),  
        ('B','B'),
        ('C','C'),
    }

    nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
    takhossus = models.ForeignKey(Takhossus, null=True, on_delete=models.SET_NULL)
    hal = models.CharField(max_length=3, blank=True, null=True)
   
    lafadz = models.CharField(max_length=200, blank=True, null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
    ustadz = models.ForeignKey(Asatidz, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
       return '%s, %s' % (self.nama, self.takhossus)




class Nubzah(models.Model):
    ajuz={
        ('juz 1','juz 1'),
        ('juz 2','juz 2'),
        ('juz 3','juz 3'),
        ('juz 4','juz 4'),
        ('juz 5','juz 5'),
        ('takmilah','takmilah'),
     }

    juz = models.CharField(choices=ajuz, max_length=30, blank=True, null=True)
    halaman = models.CharField(max_length=30, blank=True, null=True)
  
    def __str__(self):
       return self.juz
# class HalNubzah(models.Model):
#     juznubzah = models.ForeignKey(JuzNubzah, null=True, on_delete=models.SET_NULL)
#     halaman = models.CharField(max_length=30, blank=True, null=True)
  
#     def __int__(self):
#        return self.juznubzah
# class Nubzah(models.Model):
#     nubzah = models.ForeignKey(HalNubzah, null=True, on_delete=models.SET_NULL)
    
  
    # def __int__(self):
    #    return self.nubzah
# class Qorib(models.Model):
#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     halaman2 = models.IntegerField(null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     def __int__(self):
#        return self.halaman2

# class Muin(models.Model):
#     halaman3 = models.IntegerField(null=True)
  
#     def __int__(self):
#        return self.halaman3

# class Faroid(models.Model):
#     halaman4 = models.IntegerField(null=True)
  
#     def __int__(self):
#        return self.halaman4

# class Mantiq(models.Model):
#     halaman5 = models.IntegerField(null=True)

#     def __int__(self):
#        return self.halaman5
# class Arudl(models.Model):
#     halaman6 = models.IntegerField(null=True)

#     def __int__(self):
#        return self.halaman6

# class Balaghoh(models.Model):
#     halaman7 = models.IntegerField(null=True)
  
#     def __int__(self):
#        return self.halaman7

# class Qowaid(models.Model):
#     halaman8 = models.IntegerField(null=True)
   
#     def __int__(self):
#        return self.halaman8

# class Usul(models.Model):
#     halaman9 = models.IntegerField(null=True)
  
#     def __int__(self):
#        return self.halaman9





# class strNubzah(models.Model):
#     nilai={
#         ('A','A'),
#         ('B','B'),
#         ('C','C'),
#     }

#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     nubzah = models.ForeignKey(Nubzah, null=True, on_delete=models.SET_NULL)
#     # hal = models.ManyToManyField(HalNubzah)
   
#     lafadz = models.CharField(max_length=200, blank=True, null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
    
#     def __int__(self):
#        return self.nama

# class strQorib(models.Model):
#     nilai={
#         ('A','A'),
#         ('B','B'),
#         ('C','C'),
#     }

#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     halaman = models.ForeignKey(Qorib, null=True, on_delete=models.SET_NULL)
#     lafadz = models.CharField(max_length=200, blank=True, null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
  
#     def __int__(self):
#        return '%s, %s' % (self.nama, self.santri)

# class strMuin(models.Model):
#     nilai={
#         ('A','A'),
#         ('B','B'),
#         ('C','C'),
#     }

#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     halaman = models.ForeignKey(Muin, null=True, on_delete=models.SET_NULL)
#     lafadz = models.CharField(max_length=200, blank=True, null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
  
#     def __int__(self):
#        return self.nama

# class strFaroid(models.Model):
#     nilai={
#         ('A','A'),
#         ('B','B'),
#         ('C','C'),
#     }

#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     halaman = models.ForeignKey(Faroid, null=True, on_delete=models.SET_NULL)
#     lafadz = models.CharField(max_length=200, blank=True, null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
  
#     def __int__(self):
#        return self.nama

# class strMantiq(models.Model):
#     nilai={
#         ('A','A'),
#         ('B','B'),
#         ('C','C'),
#     }

#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     halaman = models.ForeignKey(Mantiq, null=True, on_delete=models.SET_NULL)
#     lafadz = models.CharField(max_length=200, blank=True, null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
  
#     def __int__(self):
#        return self.nama

# class strArudl(models.Model):
#     nilai={
#         ('A','A'),
#         ('B','B'),
#         ('C','C'),
#     }

#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     halaman = models.ForeignKey(Arudl, null=True, on_delete=models.SET_NULL)
#     lafadz = models.CharField(max_length=200, blank=True, null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
  
#     def __int__(self):
#        return self.nama

# class strBalaghoh(models.Model):
#     nilai={
#         ('A','A'),
#         ('B','B'),
#         ('C','C'),
#     }

#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     halaman = models.ForeignKey(Balaghoh, null=True, on_delete=models.SET_NULL)
#     lafadz = models.CharField(max_length=200, blank=True, null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
  
#     def __int__(self):
#        return self.nama

# class strQowaid(models.Model):
#     nilai={
#         ('A','A'),
#         ('B','B'),
#         ('C','C'),
#     }

#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     halaman = models.ForeignKey(Qowaid, null=True, on_delete=models.SET_NULL)
#     lafadz = models.CharField(max_length=200, blank=True, null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
  
#     def __int__(self):
#        return self.nama

# class strUsul(models.Model):
#     nilai={
#         ('A','A'),
#         ('B','B'),
#         ('C','C'),
#     }

#     nama = models.ForeignKey(Santri, null=True, on_delete=models.SET_NULL)
#     halaman = models.ForeignKey(Usul, null=True, on_delete=models.SET_NULL)
#     lafadz = models.CharField(max_length=200, blank=True, null=True)
#     tanggal = models.DateTimeField(auto_now_add=True, null=True)
#     predikat = models.CharField(choices=nilai, max_length=30, blank=True, null=True)
  
#     def __int__(self):
#        return self.nama

