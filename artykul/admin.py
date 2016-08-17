from .models import Kategoria, Artykul
from django.contrib import admin
import os
from PIL import Image
# Register your models here.

class KategoriaAdmin(admin.ModelAdmin):
    pass
class ArtykulAdmin(admin.ModelAdmin):
    pass
admin.site.register(Artykul, ArtykulAdmin)
admin.site.register(Kategoria, KategoriaAdmin)
# register_gallery_admin(ApartmentGallery)
