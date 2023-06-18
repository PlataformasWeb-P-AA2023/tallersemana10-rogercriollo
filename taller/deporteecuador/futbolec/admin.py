from django.contrib import admin
from futbolec.models import Equipo, Jugador, Campeonato, Campeonato3


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'username_twitter')
    search_fields = ['nombre', 'siglas']  # Pasar los campos de búsqueda como una lista

admin.site.register(Equipo, EquipoAdmin)


class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'nro_camiseta', 'sueldo', 'equipo')
    raw_id_fields = ['equipo']
    
admin.site.register(Jugador, JugadorAdmin)




class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_ausp')
    search_fields = ('nombre', 'nombre_ausp')

admin.site.register(Campeonato, CampeonatoAdmin)

class Campeonato3Admin(admin.ModelAdmin):
    list_display = ('anio', 'Equipo', 'Campeonato')
    search_fields = ('anio', 'Equipo', 'Campeonato')

admin.site.register(Campeonato3, Campeonato3Admin)
