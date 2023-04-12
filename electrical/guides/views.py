from django.shortcuts import render


def guide(request):
    return render(request, 'guides/templates/guides.html')


def competitive_exam(request):
    return render(request, 'guides/templates/competitive_examination.html')

# Create your views here.
