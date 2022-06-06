from django.contrib import admin
from  .models import pizza, empanada, bebida, postre

# Register your models here.
admin.site.register(pizza)
admin.site.register(empanada)
admin.site.register(bebida)
admin.site.register(postre)
