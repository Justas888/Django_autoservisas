from django.contrib import admin

# Register your models here.

from .models import Klientas, Marke, Modelis, Automobilis, Paslauga, Uzsakymas, UzsakymoPrekes

class UzsakymoPrekesInline(admin.TabularInline):
    model = UzsakymoPrekes
    extra = 2

class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('id', 'automobilis', 'uzsakovas', 'sukurimo_data', 'statusas', 'grazinimo_terminas')
    list_editable = ('uzsakovas', 'statusas')
    inlines = [UzsakymoPrekesInline]
    list_filter = ('statusas',)
    search_fields = ('automobilis__valst_nr',)


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'modelis', 'valst_nr')
    list_filter = ('klientas', 'modelis')
    search_fields = ('valst_nr', 'klientas__vardas')

class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')

admin.site.register(Klientas)
admin.site.register(Marke)
admin.site.register(Modelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoPrekes)