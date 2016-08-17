from django import forms
from django.forms import widgets
from sites.models import Website

class WebSiteForm(forms.ModelForm):
    class Meta:
        model = Website
        exclude = ('user', 'updated', 'site_type', 'mobile_type', 'generated')
        widgets = {
           ...
           'header_image' : forms.HiddenInput()
        }
