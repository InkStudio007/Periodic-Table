from django.urls import path
from . import views

urlpatterns = [
    path('', views.periodic_table, name='periodic_table'),
    path('H/', views.hydrogen, name='H'),
    path('Li/', views.lithium, name='Li'),
    path('Na/', views.sodium, name='Na'),
    path('K/', views.potassium, name='K'),
    path('Rb/', views.rubidium, name='Rb'),
    path('Cs/', views.cesium, name='Cs'),
    path('Fr/', views.francium, name='Fr'),
    # 2
    path('Be/', views.beryllium, name='Be'),
    path('Mg/', views.magnesium, name='Mg'),
    path('Ca/', views.calcium, name='Ca'),
    path('Sr/', views.strontium, name='Sr'),
    path('Ba/', views.barium, name='Ba'),
    path('Ra/', views.radium, name='Ra'),
    # 3
    path('Sc/', views.scandium, name='Sc'),
    path('Y/', views.yttrium, name='Y'),
    # 4
    path('Ti/', views.titanium, name='Ti'),
    path('Zr/', views.zirconium, name='Zr'),
    path('Hf/', views.hafnium, name='Hf'),
    path('Rf/', views.rutherfordium, name='Rf'),
    # 5
    path('V/', views.vanadium, name='V'),
    path('Nb/', views.nobium, name='Nb'),
    path('Ta/', views.tantalum, name='Ta'),
    path('Db/', views.dubnium, name='Db'),
    # 6
    path('Cr/', views.chromium, name='Cr'),
    path('Mo/', views.molybdenum, name='Mo'),
    path('W/', views.tungsten, name='W'),
    path('Sg/', views.seaborgium, name='Sg'),
    # 8
    path('Fe/', views.iron, name='Fe'),
    path('Ru/', views.ruthenium, name='Ru'),
    path('Os/', views.osmium, name='Os'),
    path('Hs/', views.hassium, name='Hs'),
    # 10
    path('Ni/', views.nickel, name='Ni'),
    path('Pd/', views.palladium, name='Pd'),
    path('Pt/', views.platinum, name='Pt'),
    path('Ds/', views.darmstadtium, name='Ds'),
    # 12
    path('Zn/', views.zinc, name='Zn'),
    path('Cd/', views.codmium, name='Cd'),
    path('Hg/', views.mercury, name='Hg'),
    path('Cn/', views.copernicium, name='Cn'),
    ]
