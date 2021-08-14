from django.contrib import admin
from django.urls import path, include
# from appstor.views import kontak, appstor
from django.conf.urls.static import  static
from django.conf import settings
from appstor.views import*


# from appstor.views import home_page, kontak_page, appstor_page
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', include('appstor.url')),
 path('export_xls/', ekpos, name='export_xls'),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)