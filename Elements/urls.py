from django.urls import path
from . import views

urlpatterns = [
    path('', views.periodic_table, name='periodic_table'),
    # 1
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
]
