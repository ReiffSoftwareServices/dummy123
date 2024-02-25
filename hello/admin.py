from django.contrib import admin

# Register your models here.

from .models import Firma, Ansprechpartner, Inventar, Projekt, Geruestbuch, Equipments

admin.site.register(Firma)
admin.site.register(Ansprechpartner)
admin.site.register(Inventar)
admin.site.register(Projekt)
# admin.site.register(Geruestbuch)
admin.site.register(Equipments)

@admin.register(Geruestbuch)
class GeruestbuchAdmin(admin.ModelAdmin):
    list_display=('Geruestnummer', 'Projekt', 'Kunde', 'Ansprechpartner',  'Aufbaudatum','Abmeldedatum','Preis')
    
    
    
    
    # # Geruestnummer= models.AutoField(primary_key= True)
    # Kunde= models.ForeignKey(Firma, on_delete=models.PROTECT, verbose_name= 'Firma')
    # Ansprechpartner= models.ForeignKey(Ansprechpartner, on_delete=models.PROTECT, verbose_name= 'Ansprechpartner')

    # Projekt = models.ForeignKey(Projekt, on_delete=models.PROTECT, verbose_name= 'Projekt Name')
    # Grund= models.TextField(blank= True, verbose_name= 'Grund')

    # Anlage= models.CharField(max_length= 100, blank= True, verbose_name= 'Anlage/ Equipment')
    # Ebene= models.CharField(max_length= 100, blank= True, verbose_name= 'Ebene')
    # Oertlichkeit= models.CharField(max_length= 100, blank= True, verbose_name= 'Oertlichkeit')

    # #Dates
    # Eingangsdatum= models.DateField(default = timezone.now, verbose_name= 'Eingangsdatum')
    # Aufbaudatum = models.DateField(blank = True, null = True, verbose_name= 'Aufbaudatum')
    # Abmeldedatum = models.DateField(blank = True, null = True, verbose_name= 'Abmeldedatum')

    # #Renting
    # Mietbeginn= models.DateField(blank= True, null= True, verbose_name= 'Miet-Beginn')
    # Mietende= models.DateField(blank= True, null= True, verbose_name= 'Miet-Ende')

    # #Price
    # Preis= models.DecimalField(max_digits= 12, decimal_places= 2, blank= True, null= True, verbose_name= 'Preis')
