from artykul.models import Kategoria

def pspc(request):
    return{
        'categories': Kategoria.objects.all(),
        }
