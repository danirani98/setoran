import django_filters
# from django_filters import DateFilter, CharFilter
from .models import *

class SantriFilter(django_filters.FilterSet):
    class Meta:
        model = Santri
        fields ='__all__'
        exclude = ['alamat','status','jk','marhalah',]

class UstadFilter(django_filters.FilterSet):
    class Meta:
        model = Asatidz
        fields ='__all__'
        exclude = ['alamat','status','jk', 'profile_pic']

class SetorFilter(django_filters.FilterSet):
    class Meta:
        model = Setoran
        fields ='__all__'
        exclude = ['hal','predikat','ustadz']