from django.contrib import admin

# Register your models here.

from .models import Klientas, Marke, Modelis, Automobilis, Paslauga, Uzsakymas, UzsakymoPrekes

admin.site.register(Klientas)
admin.site.register(Marke)
admin.site.register(Modelis)
admin.site.register(Automobilis)
admin.site.register(Paslauga)
admin.site.register(Uzsakymas)
admin.site.register(UzsakymoPrekes)