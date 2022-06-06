"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pizza_web.views import pizza_view, empanada_view, bebida_view, postre_view, index_view, agregar_pizza_view, agregar_empanada_view, agregar_bebida_view, agregar_postre_view, buscar_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('pizzas/', pizza_view, name='pizzas'),
    path('empanadas/', empanada_view, name='empanadas'),
    path('bebidas/', bebida_view, name='bebidas'),
    path('postres/', postre_view, name='postres'),
    path('agregar_pizza/', agregar_pizza_view, name='agregar_pizza'),
    path('agregar_empanada/', agregar_empanada_view, name='agregar_empanada'),
    path('agregar_bebida/', agregar_bebida_view, name='agregar_bebida'),
    path('agregar_postre/', agregar_postre_view, name='agregar_postre'),
    path('buscar/', buscar_view,  name = 'buscar')
    
]
