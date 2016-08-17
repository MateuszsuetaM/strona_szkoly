from artykul.models import Kategoria, Artykul

def cats(context):
    return render{'cats', context_instance= Kategoria.objects.all()}
