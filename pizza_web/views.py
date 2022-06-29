from genericpath import exists
from django.shortcuts import render
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate, login
# Create your views here.
from pizza_web.models import pizza, empanada, bebida, postre
from pizza_web.forms import pizza_form, empanada_form, bebida_form, postre_form

# Create your views here.

def login_view(request):
    if  request.method== 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data ['password']
            user = authenticate(username=username, password = password)

            if user is not None:
                login(request, user)
                context = {'message': f'Bienvenido {username}'}
                return  render(request, 'index.html', context = context)


    else:
        form = AuthenticationForm()
        context= {'form': form}
        return render(request, 'login.html', context=context)


def pizza_view (request):
    pizzas= pizza.objects.all()
    context={'pizzas': pizzas}
    return render (request, 'pizzas.html', context=context)

def empanada_view (request):
    empanadas= empanada.objects.all()
    context={'empanadas': empanadas}
    return render (request, 'empanadas.html', context=context)

def bebida_view (request):
    bebidas= bebida.objects.all()
    context={'bebidas': bebidas}
    return render (request, 'bebidas.html', context=context)

def postre_view (request):
    postres= postre.objects.all()
    context={'postres': postres}
    return render (request, 'postres.html', context=context)

def index_view (request):
    context={}
    return render (request, 'index.html', context=context)
    
def agregar_pizza_view (request):
    if request.method == 'GET':
        form = pizza_form()
        context = {'form':form}
        return render(request, 'agregar_pizza.html', context=context)
    else:
        form = pizza_form(request.POST)
        if form.is_valid():
            new_pizza= pizza.objects.create(
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                ingredientes = form.cleaned_data['ingredientes'],
                apto_delivery = form.cleaned_data['apto_delivery'],
                vegana = form.cleaned_data['vegana'],
            )
            context ={'new_pizza':new_pizza}
        else:
            context = {'errors': form.errors}
        return render(request, 'agregar_pizza.html', context=context)

def agregar_empanada_view (request):
    if request.method == 'GET':
        form = empanada_form()
        context = {'form':form}
        return render(request, 'agregar_empanada.html', context=context)
    else:
        form = empanada_form(request.POST)
        if form.is_valid():
            new_empanada= empanada.objects.create(
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                ingredientes = form.cleaned_data['ingredientes'],
                apto_delivery = form.cleaned_data['apto_delivery'],
            )
            context ={'new_empanada':new_empanada}
        else:
            context = {'errors': form.errors}        
        return render(request, 'agregar_empanada.html', context=context)

def agregar_bebida_view (request):
    if request.method == 'GET':
        form = bebida_form()
        context = {'form':form}
        return render(request, 'agregar_bebida.html', context=context)
    else:
        form = bebida_form(request.POST)
        if form.is_valid():
            new_bebida= bebida.objects.create(
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                apto_delivery = form.cleaned_data['apto_delivery'],
            )
            context ={'new_bebida':new_bebida}
        else:
            context = {'errors': form.errors}
        return render(request, 'agregar_bebida.html', context=context)

def agregar_postre_view (request):
    if request.method == 'GET':
        form = postre_form()
        context = {'form':form}
        return render(request, 'agregar_postre.html', context=context)
    else:
        form = postre_form(request.POST)
        if form.is_valid():
            new_postre= postre.objects.create(
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                apto_delivery = form.cleaned_data['apto_delivery'],
                gluten_free  =form.cleaned_data ['gluten_free']
            )
            context ={'new_postre':new_postre}
        else:
            context = {'errors': form.errors}
        return render(request, 'agregar_postre.html', context=context)

def buscar_view(request):
    #print(request.GET)
    producto_busqueda = request.GET['search']
    buscar_pizza = pizza.objects.filter(nombre__icontains = producto_busqueda)
    buscar_empanada = empanada.objects.filter(nombre__icontains = producto_busqueda)
    buscar_bebida = bebida.objects.filter(nombre__icontains = producto_busqueda)
    buscar_postre= postre.objects.filter(nombre__icontains = producto_busqueda)
    
    if buscar_pizza.exists() or buscar_empanada.exists() or buscar_bebida.exists() or buscar_postre.exists():
        context = {'buscar_pizza':buscar_pizza, 'buscar_empanada': buscar_empanada, 'buscar_bebida': buscar_bebida, 'buscar_postre': buscar_postre}
    else:
        context= {'errors': f"Disculpe, no encontramos un producto con el texto {producto_busqueda}."}
    return render(request, 'buscar.html', context = context)
