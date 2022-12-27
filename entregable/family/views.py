from django.shortcuts import render
from django.http import HttpResponse
from family.models import family

# Create your views here.
def create_family(request):
    new_family = family.objects.create(name ='Lautaro', age= 12, study= True )
    print(new_family)
    return HttpResponse ('se creo el nuevo familiar')

def list_family(request):
    all_family = family.objects.all()
    print(all_family)
    context = {
        'family': all_family,
    }
    return render(request, 'list_family.html', context=context )