from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from django.views import generic
from .models import Uzsakymas, Automobilis, Paslauga

# Create your views here.

def index(request):
    paslaugu_kiekis = Paslauga.objects.count()
    uzsakymu_kiekis = Uzsakymas.objects.count()
    atliktu_uzsakymu_kiekis = Uzsakymas.objects.filter(statusas=Uzsakymas.COMPLETED).count()
    automobiliu_kiekis = Automobilis.objects.count()

    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'uzsakymu_kiekis': uzsakymu_kiekis,
        'atliktu_uzsakymu_kiekis': atliktu_uzsakymu_kiekis,
        'automobiliu_kiekis': automobiliu_kiekis
    }

    return render(request, 'index.html', context=context)

def automobiliai(request):
    visi_automobiliai = Automobilis.objects.all()
    context = {'automobiliai': visi_automobiliai}
    return render(request, 'automobiliai.html', context=context)

def automobilis(request, automobilis_id):
    automobilis = get_object_or_404(Automobilis, pk=automobilis_id)
    context = {'automobilis': automobilis}
    return render(request, 'automobilis.html', context=context)

class UzsakymaiListView(generic.ListView):
    model = Uzsakymas
    context_object_name = 'uzsakymai'
    template_name = 'uzsakymai.html'

    def get_queryset(self):
        return Uzsakymas.objects.all()

class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    context_object_name = 'uzsakymas'
    template_name = 'uzsakymas.html'
