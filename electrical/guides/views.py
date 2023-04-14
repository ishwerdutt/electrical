from django.shortcuts import render


def guide(request):
    return render(request, 'guides/templates/guides.html')

def gsoc(request):
    return render(request, 'guides/templates/gsoc.html')

def noc(request):
    return render(request, 'guides/templates/noc.html')

def gate(request):
    return render(request, 'guides/templates/gate.html')


# Create your views here.
