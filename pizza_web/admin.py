from django.contrib import admin
from  .models import pizza, empanada, bebida, postre

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

