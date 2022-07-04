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
from pizza_web.views import pizza_view, empanada_view, bebida_view, postre_view, index_view, agregar_pizza_view, agregar_empanada_view, agregar_bebida_view, agregar_postre_view, buscar_view, login_view, logout_view, register_view, pizza_detail_view, bebida_detail_view, empanada_detail_view, postre_detail_view, eliminar_pizza_view, eliminar_bebida_view, eliminar_empanada_view, eliminar_postre_view, update_pizza, update_empanada,  update_bebida, update_postre, editar_usuario, perfil_usuario_view, about_view, update_portada_view, update_portada_secundaria__view, elements_view
from django.conf import settings
from django.conf.urls.static import static



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
    path('buscar/', buscar_view,  name = 'buscar'),
    path ('accounts/login/', login_view, name= 'login'),
    path ('logout/', logout_view, name= 'logout'),
    path ('accounts/signup/', register_view, name= 'register'),
    path ('pizza_detail/<int:pk>/', pizza_detail_view, name = 'pizza_detail'),
    path ('bebida_detail/<int:pk>/', bebida_detail_view, name = 'bebida_detail'),
    path ('empanada_detail/<int:pk>/', empanada_detail_view, name = 'empanada_detail'),
    path ('postre_detail/<int:pk>/', postre_detail_view, name = 'postre_detail'),
    path ('eliminar_pizza/<int:pk>/', eliminar_pizza_view, name = 'eliminar_pizza'),
    path ('eliminar_empanada/<int:pk>/', eliminar_empanada_view, name = 'eliminar_empanada'),
    path ('eliminar_bebida/<int:pk>/', eliminar_bebida_view, name = 'eliminar_bebida'),
    path ('eliminar_postre/<int:pk>/', eliminar_postre_view, name = 'eliminar_postre'),
    path ('update_pizza/<int:pk>/', update_pizza.as_view(), name = 'update_pizza'),
    path ('update_empanada/<int:pk>/', update_empanada.as_view(), name = 'update_empanada'),
    path ('update_bebida/<int:pk>/', update_bebida.as_view(), name = 'update_bebida'),
    path ('update_postre/<int:pk>/', update_postre.as_view(), name = 'update_postre'),
    path ('accounts/update_user/', editar_usuario, name = 'update_user'),
    path ('accounts/profile/', perfil_usuario_view, name = 'perfil_usuario'),
    path ('about/', about_view, name = 'about'),
    path ('update_portada/<int:pk>/', update_portada_view.as_view(), name = 'update_portada'),
    path ('update_portada_secundaria/<int:pk>/', update_portada_secundaria__view.as_view(), name = 'update_portada_secundaria'),
    path ('elements', elements_view, name= 'elements'),
]  + static (settings.MEDIA_URL, document_root  = settings.MEDIA_ROOT)

