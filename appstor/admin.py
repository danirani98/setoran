from django.contrib import admin



# Register your models here.
from .models import *
# from .models import ket
from import_export.admin import ImportExportModelAdmin


class BookAdmin(ImportExportModelAdmin):
   pass

admin.site.register(Ket, ImportExportModelAdmin)

admin.site.register(Santri)
admin.site.register(Takhossus)
admin.site.register(Setoran)
admin.site.register(Asatidz)


# admin.site.register(Qorib)
# admin.site.register(Muin)
# admin.site.register(Faroid)
# admin.site.register(Balaghoh)
# admin.site.register(Mantiq)
# admin.site.register(Arudl)
# admin.site.register(Qowaid)
# admin.site.register(Usul)
# admin.site.register(strNubzah)
# admin.site.register(strQorib)
# admin.site.register(strMuin)
# admin.site.register(strFaroid)
# admin.site.register(strMantiq)
# admin.site.register(strBalaghoh)
# admin.site.register(strArudl)
# admin.site.register(strQowaid)
# admin.site.register(strUsul)


