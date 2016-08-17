from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import os
# from django.contrib.auth.models import User
# from galleries.models import Gallery
# from imagekit.models import ImageSpec
# from imagekit.processors import Crop
# Create your models here.


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=20, null=False, blank=False, unique=True)
#    owner = models.ForeignKey(User, null=False, blank=False)
#    opis = models.TextField(null=False, blank=False)

    def __unicode__(self):
        return self.nazwa


class Artykul(models.Model):
    tytul = models.CharField(max_length=30, null=False, blank=False)
    teaser = models.CharField(max_length=50, null=True, blank=True)
    zawartosc = models.TextField(max_length=200, null=False, blank=False)
    data_dodania = models.DateTimeField(default=timezone.now)
    data_zmiany = models.DateTimeField(default=timezone.now)
    kategoria = models.ForeignKey('Kategoria')
    wyroznione = models.BooleanField(blank=False, null=False)
    autor = models.ForeignKey('auth.User')
    obrazy = models.ImageField(upload_to='galleries/', blank=True)
    # miniaturka=models.ImageSpec([Crop(60, 60)], image_field='obrazy')

    def __unicode__(self):
        return self.tytul

# class ApartmentGallery(Gallery):
#
#     class GalleryMeta:
#         member_models = [Artykul.miniaturka]

def header_image_file_name(instance, filename):
    cat = Image_category.objects.get(id=instance.category.id)
    n = cat.name
    n = n.lower().replace (" ", "_")
    return os.path.join(
      "template_images", "headers", "%s" % n, "large", filename)

def header_image_thumbnail_file_name(instance, filename):
    cat = Image_category.objects.get(id=instance.category.id)
    n = cat.name
    n = n.lower().replace (" ", "_")
    return os.path.join(
      "template_images", "headers", "%s" % n, "thumbs", filename)

class Image_category(models.Model):
    name = models.CharField(max_length=35)

    def __unicode__(self):
        return self.name

class Header_image(models.Model):
    category = models.ForeignKey(Image_category)
    image = models.ImageField(upload_to=header_image_file_name)
    thumbnail = models.ImageField(upload_to=header_image_thumbnail_file_name, blank=True,null=True)

    def __unicode__(self):
        return str(self.image)

# class Website(models.Model):
#     user = models.ForeignKey(User)
#     header_image = models.ForeignKey(Header_image)
#     domain_name = models.CharField(max_length=75)
#     site_type = models.ForeignKey(Site_type)
