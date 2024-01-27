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
    # 7
    path('Mn/', views.manganese, name='Mn'),
    path('Tc/', views.technetium, name='Tc'),
    path('Re/', views.rhenium, name='Re'),
    path('Bh/', views.bohrium, name='Bh'),
    # 8
    path('Fe/', views.iron, name='Fe'),
    path('Ru/', views.ruthenium, name='Ru'),
    path('Os/', views.osmium, name='Os'),
    path('Hs/', views.hassium, name='Hs'),
    # 9
    path('Co/', views.cobalt, name='Co'),
    path('Rh/', views.rhodium, name='Rh'),
    path('Ir/', views.iridium, name='Ir'),
    path('Mt/', views.meitnerium, name='Mt'),
    # 10
    path('Ni/', views.nickel, name='Ni'),
    path('Pd/', views.palladium, name='Pd'),
    path('Pt/', views.platinum, name='Pt'),
    path('Ds/', views.darmstadtium, name='Ds'),
    # 11
    path('Cu/', views.copper, name='Cu'),
    path('Ag/', views.silver, name='Ag'),
    path('Au/', views.gold, name='Au'),
    path('Rg/', views.roentgenium, name='Rg'),
    # 12
    path('Zn/', views.zinc, name='Zn'),
    path('Cd/', views.cadmium, name='Cd'),
    path('Hg/', views.mercury, name='Hg'),
    path('Cn/', views.copernicium, name='Cn'),
    # 13
    path('B/', views.boron, name='B'),
    path('Al/', views.aluminum, name='Al'),
    path('Ga/', views.gallium, name='Ga'),
    path('In/', views.indium, name='In'),
    path('Tl/', views.thallium, name='Tl'),
    path('Nh/', views.nihonium, name='Nh'),
    # 14
    path('C/', views.carbon, name='C'),
    path('Si/', views.silicon, name='Si'),
    path('Ge/', views.germanium, name='Ge'),
    path('Sn/', views.tin, name='Sn'),
    path('Pb/', views.lead, name='Pb'),
    path('Fl/', views.flerovium, name='Fl'),
    # 15
    path('N/', views.nitrogen, name='N'),
    path('P/', views.phosphorus, name='P'),
    path('As/', views.arsenic, name='As'),
    path('Sb/', views.antimony, name='Sb'),
    path('Bi/', views.bismuth, name='Bi'),
    path('Mc/', views.moscovium, name='Mc'),
    # 16
    path('O/', views.oxygen, name='O'),
    path('S/', views.sulfur, name='S'),
    path('Se/', views.selenium, name='Se'),
    path('Te/', views.tellurium, name='Te'),
    path('Po/', views.polonium, name='Po'),
    path('Lv/', views.livermorium, name='Lv'),
    # 17
    path('F/', views.fluorine, name='F'),
    path('Cl/', views.chlorine, name='Cl'),
    path('Br/', views.bromine, name='Br'),
    path('I/', views.Iodine, name='I'),
    path('At/', views.astatine, name='At'),
    path('Ts/', views.tennessine, name='Ts'),
    # 18
    path('He/', views.helium, name='He'),
    path('Ne/', views.neon, name='Ne'),
    path('Ar/', views.argon, name='Ar'),
    path('Kr/', views.krypton, name='Kr'),
    path('Xe/', views.xenon, name='Xe'),
    path('Rn/', views.radon, name='Rn'),
    path('Og/', views.oganesson, name='Og'),
    ]
