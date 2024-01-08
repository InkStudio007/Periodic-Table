from django.shortcuts import render

# Create your views here.


def periodic_table(request):
    return render(request, 'periodic_table.html')


# 1


def hydrogen(request):
    return render(request, '1/Hydrogen.html')


def lithium(request):
    return render(request, '1/Lithium.html')


def sodium(request):
    return render(request, '1/Sodium.html')


def potassium(request):
    return render(request, '1/Potassium.html')


def rubidium(request):
    return render(request, '1/Rubidium.html')


def cesium(request):
    return render(request, '1/Cesium.html')


def francium(request):
    return render(request, '1/Francium.html')


# 2


def beryllium(request):
    return render(request, '2/Beryllium.html')


def magnesium(request):
    return render(request, '2/Magnesium.html')


def calcium(request):
    return render(request, '2/Calcium.html')


def strontium(request):
    return render(request, '2/Strontium.html')


def barium(request):
    return render(request, '2/Barium.html')


def radium(request):
    return render(request, '2/Radium.html')


