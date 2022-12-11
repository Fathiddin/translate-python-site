from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'index.html')

def list(request):
    lists = List.objects.all()
    context = {
        'lists':lists
    }
    return render(request, 'list.html', context)

def add(request):
    return render(request, 'add.html')

def addlist(request):
    x = request.POST['uzb']
    y = request.POST['eng']
    contact = List(uzb=x, eng=y)
    contact.save()
    return render(request, 'index.html')


def search(request):
    q = request.GET.get("query")
    # print(type(q))
    if len(q) >= 2:
        query = List.objects.filter(
            Q(uzb__icontains=q) | Q(eng__icontains=q)
        )
        return render(request, "result.html", {"lists": query})
    return render(request, "result.html")
