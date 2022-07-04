from django.contrib import admin
from  .models import pizza, empanada, bebida, postre, portada, secundaria_portada, about_portada

# Register your models here.
@admin.register(pizza)
class pizzaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'apto_delivery']

@admin.register(empanada)
class empanadaAdmin(admin.ModelAdmin):
    list_display=['nombre', 'precio', 'apto_delivery']

@admin.register(bebida)
class bebidaAdmin(admin.ModelAdmin):
    list_display=['nombre', 'precio', 'apto_delivery']

@admin.register(postre)
class postreAdmin(admin.ModelAdmin):
    list_display=['nombre', 'precio', 'apto_delivery']

@admin.register(portada)
class portadaAdmin(admin.ModelAdmin):
    list_display=['id','image', 'description']

@admin.register(secundaria_portada)
class portada_secundariaAdmin(admin.ModelAdmin):
    list_display=['id','image', 'description']

@admin.register(about_portada)
class portada_aboutAdmin(admin.ModelAdmin):
    list_display=['id','image', 'description']
