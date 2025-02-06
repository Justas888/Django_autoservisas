from datetime import datetime

from django.db import models

# Create your models here.

class Klientas(models.Model):
    vardas = models.CharField('Vardas', max_length=100)
    pavarde = models.CharField('Pavardė', max_length=100)
    email = models.EmailField('Email', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Klientas'
        verbose_name_plural = 'Klientai'

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"

class Marke(models.Model):
    marke = models.CharField('Markė',max_length=100)

    def __str__(self):
        return f"{self.marke}"

class Modelis(models.Model):
    marke = models.ForeignKey(Marke, on_delete=models.CASCADE)
    modelis = models.CharField('Modelis', max_length=100)

    class Meta:
        verbose_name = 'Modelis'
        verbose_name_plural = 'Modeliai'


    def __str__(self):
        return f"{self.marke} {self.modelis}"


class Automobilis(models.Model):
    klientas = models.ForeignKey(Klientas, on_delete=models.CASCADE)
    modelis = models.ForeignKey(Modelis, on_delete=models.CASCADE)
    metai = models.IntegerField('Pagaminimo metai')
    valst_nr = models.CharField('Valstybinis numeris',max_length=20)
    foto = models.ImageField('Foto', upload_to='foto', null=True, blank=True)

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'

    def __str__(self):
        return f"{self.valst_nr} {self.modelis} {self.metai}"

class Paslauga(models.Model):
    pavadinimas = models.CharField('Paslaugos pavadinimas',max_length=200)
    aprasymas = models.TextField('Paslaugos aprašymas', max_length=1300)
    kaina = models.IntegerField('Paslaugos kaina', default=0)

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'

    def __str__(self):
        return f"Paslauga: {self.pavadinimas}, kaina: {self.kaina}"



class Uzsakymas(models.Model):
    sukurimo_data = models.DateTimeField('Sukurimo data', default=datetime.now, null=True, blank=True)
    automobilis = models.ForeignKey(Automobilis, on_delete=models.CASCADE)
    imoketa_suma = models.IntegerField('Įmokėta suma')

    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CANCELLED = 3

    STATUS_CHOICES = [
        (NEW, 'Naujas'),
        (IN_PROGRESS, 'Vykdomas'),
        (COMPLETED, 'Įvykdytas'),
        (CANCELLED, 'Atšauktas'),
    ]

    statusas = models.IntegerField('Statusas',
                                 choices=STATUS_CHOICES,
                                 default=NEW,
                                 blank=True,
                                 help_text='Užsakymo statusas')

    # @property
    # def bendra_suma(self):
    #     viso = sum([item.paslauga.kaina * item.kiekis for item in self.uzsakymo_prekes.all()])
    #     return viso

    class Meta:
        verbose_name = 'Uzsakymas'
        verbose_name_plural = 'Uzsakymai'

    def __str__(self):
        return f"{self.automobilis} {self.sukurimo_data}"

class UzsakymoPrekes(models.Model):
    kiekis = models.IntegerField()
    uzsakymas = models.ForeignKey(Uzsakymas, on_delete=models.CASCADE, related_name="uzsakymo_prekes")
    paslauga = models.ForeignKey(Paslauga, on_delete=models.CASCADE)

    # @property
    # def paslaugu_kaina(self):
    #     return self.paslauga.kaina * self.kiekis

    class Meta:
        verbose_name = 'Uzsakymo_Preke'
        verbose_name_plural = 'Uzsakymų_Prekes'

    def __str__(self):
        return f"{self.uzsakymas} {self.paslauga} {self.kiekis}"





