# from django import forms
from django.forms import ModelForm
from .models import Asatidz
from .models import Santri
from .models import Setoran, Ket
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.admin import widgets   

class SantriForm(ModelForm):
    # tanggal_lahir = forms.DateTimeField(default= datetimeTextInput)
    class Meta:
      model = Santri
      fields= '__all__'
      # widgets = {
        # 'nama': forms.CharField(attrs={'class': 'form-control'}),
        # 'tempat_lahir': forms.CharField(
        #                       attrs={'class': 'form-control'},
        #                       widget=forms.Textare()),
        # 'tanggal_lahir': forms.DateTimeField(attrs={'class': 'form-control'}),
        #   }
        # labels = {
        #   'jenis_kelamin': 'jenis kelamin',
        #   }
        # def __init__(self, *args, **kwargs):
        #    super(SantriForm, self).__init__(*args, **kwargs)
        #    self.fields['tanggal_lahir'].widget = widgets.AdminDateWidget()
        #    self.fields['tanggal_lahir'].widget = widgets.AdminTimeWidget()
        #    self.fields['tanggal_lahir'].widget = widgets.AdminSplitDateTime()
        # 
class Setorank(ModelForm):
    class Meta:
      model = Setoran
      fields= '__all__'

class KetForm(ModelForm):
    class Meta:
      model = Ket
      fields= '__all__'

class AsatidzForm(ModelForm):
    class Meta:
      model = Asatidz
      fields= '__all__'

class RegisterForm(UserCreationForm):
    # email = forms.EmailField()
    class Meta:
         model = User
         fields= ['username','email','password1','password2']