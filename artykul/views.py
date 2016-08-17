from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Kategoria, Artykul
# Create your views here.

def kategoria(request):
    kategoria = Kategoria.objects.all()
    context = {'kategoria': kategoria}
    return render(request, 'artykul/artykul.html', context)

def category(request, pk):
    category = get_object_or_404(Kategoria, pk=pk)
    context = {'category': category}
    return render(request, 'artykul/kategorie.html', context)

def lista(request):
    lista = Kategoria.objects.all().order_by('pk')#.filter(nazwa).order_by('nazwa')
    return render(request, 'artykul/kategoria_detail.html', {'lista': lista})

def artykul(request, pk):
    artykul = get_object_or_404(Artykul, pk=pk)
    context = {'artykul': artykul}
    return render(request, 'artykul/category_detail.html', context)

def wszystkie(request):
    wszystkie = Artykul.objects.all()
    context = {'wszystkie': wszystkie}
    return render(request, 'artykul/kategorie.html', context)

def home(request):
    # home = Artykul.objects.all()
    # context = {'home': home}
    return render(request, 'home.html')#, context)
