from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class LogMessage(models.Model):
    message = models.CharField(max_length=300, blank=True, null=True, help_text="xxx")
    name = models.CharField(max_length=100, blank=True, null=True, help_text="yyy")
    source = models.CharField(max_length=2, blank=True, null=True, help_text="yyx")
    log_date = models.DateTimeField("date logged", blank=True, null=True, help_text="yxcv")
    
    def __str__(self):
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged {date.strftime('%A, %d %B, %Y at %X')}"
   
class Firma(models.Model):
    Name= models.CharField(max_length= 100, blank= False, verbose_name= 'Firma')
    Postleitzahl= models.CharField(max_length= 8, blank = True, verbose_name = 'Postleitzahl')
    Stadt= models.CharField(max_length= 30, blank = True, verbose_name = 'Stadt')
    Strasse= models.CharField(max_length= 30, blank = True, verbose_name = 'Strasse')
    Email= models.EmailField(max_length = 254, blank= True, verbose_name = 'Firma Email')
    Telefon= models.CharField(max_length= 30, blank = True, verbose_name = 'Telefon Firma')
    
    class Meta:
        verbose_name_plural= 'Firmenliste'
        
    def __str__(self):
        return '{}'.format(self.Name)

class Ansprechpartner(models.Model):
    Nachname= models.CharField(max_length = 50, blank = True,  verbose_name = 'Nachname')
    Vorname= models.CharField(max_length = 50, blank = True, verbose_name = 'Vorname')
    Email= models.EmailField(max_length =254, blank = True, verbose_name = 'Email Ansprechpartner')
    Telefon= models.CharField(max_length = 20, blank = True, verbose_name = 'Telefon Ansprechpartner')
    Firma= models.ForeignKey(Firma, on_delete=models.PROTECT, verbose_name= 'Firma')

    class Meta:
        verbose_name_plural = 'Ansprechpartner'

    def __str__(self):
        return  '{}, {}'.format(self.Nachname, self.Vorname)

class Inventar(models.Model):

    Name = models.CharField(max_length = 50, verbose_name= 'Bauteil')
    Einheit= models.CharField(max_length= 50, verbose_name= 'Einheit')
    Beschreibung = models.TextField(blank = True, verbose_name = 'Beschreibung')
    Preis = models.DecimalField(max_digits = 7, decimal_places = 2, blank = True, null = True, verbose_name= 'Preis') ## Not sure whether they can be zero!

    # Miete
    Einheit_Miete= models.CharField(max_length= 50, verbose_name= 'Einheit Miete')
    Beschreibung_Miete= models.CharField(max_length= 50, verbose_name= 'Beschreibung Miete')
    Preis_Miete= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Preis Miete')


    class Meta:
        verbose_name_plural= 'Leistungsverzeichnis'

    def __str__(self):
        return '{}'.format(self.Name)   
    
class Projekt(models.Model):

    ''' Table just for creating the project name '''

    Project_Name= models.CharField(max_length= 50, primary_key= True, verbose_name= 'Projekt Name')

    class Meta:
        verbose_name_plural= 'Projekte'

    def __str__(self):
        return '{}'.format(self.Project_Name)

class Geruestbuch(models.Model):
    # PK
    Geruestnummer= models.AutoField(primary_key= True, help_text="Die Gerüstnummer wird automatisch erzeugt.")
    
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
        verbose_name_plural= 'Geruestbuch'


    def __str__(self):
        return '{} - Gerüst {}'.format(self.Projekt, self.Geruestnummer) 
    
    @property
    def Mietwochen(self):
        if (self.Aufbaudatum is not None) and (self.Abmeldedatum is not None):
            time_diff= (self.Abmeldedatum- self.Aufbaudatum).days
            return int(round(time_diff/ 7)- 6)                                     # Set to six weeks now
        else:
            return None


    # Get the status of the Project
    @property
    def Status(self):
        if (self.Abmeldedatum is not None) and (self.Abmeldedatum < date.today()):
            return 'Abgeschlossen'
        else:
            return 'Laufend'
    def save(self, *args, **kwargs):
        '''Calculating the price per Geruestnummer'''
        #1. Getting all equipment from geruestnummer and the corresponding prices.
        query= Equipments.objects.filter(Geruestnummer= self.Geruestnummer).values_list('Equipment' ,flat= True)    #Output= <QuerySet [1, 2, 1, 2]>, which represents the equipment_id per geruestnummer
        preise= []
        for i in query:
            preise.append(Inventar.objects.filter(id= i).values_list('Preis', flat= True)[0])

        #2. Getting the amount per equipment
        query= Equipments.objects.filter(Geruestnummer= self.Geruestnummer).values_list('Laenge', 'Breite', 'Hoehe', 'Stueck', 'Stunde')
        amount= []
        for i in query:
            if (i[0] is not None) and (i[1] is not None) and (i[2] is not None):  #Laenge* Breite* Hoehe
                amount.append(i[0]* i[1]* i[2])
            elif ((i[3] is not None) and (i[4] is not None)): #Not sure whether this is required!
                amount.append(i[3]* i[4])
            else:
                amount.append(0)
        #3. amount= (1,2), preise= (2,3). Elementwise multipilication of the two lists. If None a zero is assigned!
        output= []
        for i in range(len(amount)):
            if (amount[i] is not None) and (preise[i] is not None):
                output.append(amount[i]* preise[i])
            else:
                output.append(0)
        output= sum(output)

        self.Preis= output
        super(Geruestbuch, self).save(*args, **kwargs)

    @property
    def Miete():
        pass

class Equipments(models.Model):

    '''
    Equipment per Geruestnummer
    '''
       
    # FK
    Geruestnummer= models.ForeignKey(Geruestbuch, on_delete=models.PROTECT, verbose_name= 'Geruestnummer')
    Equipment= models.ForeignKey(Inventar, on_delete=models.PROTECT, verbose_name= 'Inventar')

    #Metrics
    Laenge= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Laenge')
    Breite= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Breite')
    Hoehe= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Hoehe')
    Stueck= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Stueck')
    Stunde= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Stunde')


    class Meta:
        verbose_name_plural= 'Equipment'
        
    def __str__(self):
        return '{} - {} - {} Stk. {}x{}x{} ({}h)'.format(self.Geruestnummer, self.Equipment, self.Stueck, self.Laenge, self.Breite, self.Hoehe, self.Stunde) 