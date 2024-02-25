# from traceback import format_stack
from django import forms
from hello.models import LogMessage, Geruestbuch

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message", "name")
        
class LogMessageForm2(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message", "name", "source")

class AnmeldungForm(forms.ModelForm):
    class Meta:
        model = Geruestbuch
        fields = ("Kunde", "Ansprechpartner","Projekt", "Grund","Anlage","Ebene","Oertlichkeit","Aufbaudatum","Abmeldedatum")
        
        widgets = {
            'Kunde': forms.Select(attrs={'class':'form-control'}),
            'Ansprechpartner': forms.Select(attrs={'class':'form-control'}),
            'Projekt': forms.Select(attrs={'class':'form-control'}),
            'Grund': forms.TextInput(attrs={'class':'form-control'}),
            'Anlage': forms.TextInput(attrs={'class':'form-control'}),
            'Ebene': forms.TextInput(attrs={'class':'form-control'}),
            'Oertlichkeit': forms.TextInput(attrs={'class':'form-control'}),
            'Aufbaudatum': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'Abmeldedatum': forms.SelectDateWidget(attrs={'class':'form-control'})
        }
        
        
    """ #         # PK
    # Geruestnummer= models.AutoField(primary_key= True, help_text="Die Gerüstnummer wird automatisch erzeugt.")
    
    # FK
    Kunde= models.ForeignKey(Firma, on_delete=models.PROTECT, verbose_name= 'Firma')
    Ansprechpartner= models.ForeignKey(Ansprechpartner, on_delete=models.PROTECT, verbose_name= 'Ansprechpartner')
    Projekt = models.ForeignKey(Projekt, on_delete=models.PROTECT, verbose_name= 'Projekt Name')
    
    Grund= models.TextField(blank= True, verbose_name= 'Grund', help_text="Kurze Begründung warum das Gerüst angefordert wird.")
    Anlage= models.CharField(max_length= 100, blank= True, verbose_name= 'Anlage/ Equipment')
    Ebene= models.CharField(max_length= 100, blank= True, verbose_name= 'Ebene')
    Oertlichkeit= models.CharField(max_length= 100, blank= True, verbose_name= 'Oertlichkeit')

    #Dates
    Eingangsdatum= models.DateField(default = timezone.now, verbose_name= 'Eingangsdatum')
    Aufbaudatum = models.DateField(blank = True, null = True, verbose_name= 'Aufbaudatum')
    Abmeldedatum = models.DateField(blank = True, null = True, verbose_name= 'Abmeldedatum')

    #Renting
    Mietbeginn= models.DateField(blank= True, null= True, verbose_name= 'Miet-Beginn')
    Mietende= models.DateField(blank= True, null= True, verbose_name= 'Miet-Ende')

    #Price
    Preis= models.DecimalField(max_digits= 12, decimal_places= 2, blank= True, null= True, verbose_name= 'Preis')

    class Meta:
        verbose_name_plural= 'Geruestbuch' """