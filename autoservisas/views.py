from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from django.views import generic
from .models import Uzsakymas, Automobilis, Paslauga
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    paslaugu_kiekis = Paslauga.objects.count()
    uzsakymu_kiekis = Uzsakymas.objects.count()
    atliktu_uzsakymu_kiekis = Uzsakymas.objects.filter(statusas=Uzsakymas.COMPLETED).count()
    automobiliu_kiekis = Automobilis.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits +1

    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'uzsakymu_kiekis': uzsakymu_kiekis,
        'atliktu_uzsakymu_kiekis': atliktu_uzsakymu_kiekis,
        'automobiliu_kiekis': automobiliu_kiekis,
        'num_visits_t': num_visits
    }

    return render(request, 'index.html', context=context)

def automobiliai(request):
    visi_automobiliai = Automobilis.objects.all()
    paginator = Paginator(visi_automobiliai, 8)
    page_number = request.GET.get('page')
    paged_automobiliai = paginator.get_page(page_number)
    context = {'automobiliai': paged_automobiliai}
    return render(request, 'automobiliai.html', context=context)

def automobilis(request, automobilis_id):
    automobilis = get_object_or_404(Automobilis, pk=automobilis_id)
    context = {'automobilis': automobilis}
    return render(request, 'automobilis.html', context=context)

class UzsakymaiListView(generic.ListView):
    model = Uzsakymas
    context_object_name = 'uzsakymai'
    template_name = 'uzsakymai.html'
    paginate_by = 5

    def get_queryset(self):
        return Uzsakymas.objects.all()

class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    context_object_name = 'uzsakymas'
    template_name = 'uzsakymas.html'



def search(request):
    query = request.GET.get('search_text')
    search_results = Automobilis.objects.filter(
        Q(klientas__vardas__icontains=query) |
        Q(klientas__pavarde__icontains=query) |
        Q(modelis__modelis__icontains=query) |
        Q(valst_nr__icontains=query)
    )
    context = {'query': query, 'automobiliai': search_results}
    return render(request, 'automobiliai.html', context)

