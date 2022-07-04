from django import forms
from pizza_web.models import pizza, empanada, bebida, postre, portada, about_portada, secundaria_portada
from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class User_registration_form (UserCreationForm):
    username = forms.CharField(label='Nombre de usuario:', max_length= 15, required=True)
    first_name = forms.CharField(label='Nombre:', max_length= 15, required=True)
    last_name= forms.CharField(label='Apellido:', max_length= 15, required=True)
    email = forms.EmailField  (label = 'E-mail')
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    image = forms.ImageField(label= 'Foto (opcional)', required=False)
    description= forms.CharField(label='Descripción:', max_length= 30, required=False)
    link= forms.CharField(label='Link:', max_length= 25, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' , 'image', 'description', 'link']
        help_texts = {k:'' for k in fields} 

class User_edit_form (UserCreationForm):
    first_name = forms.CharField(label='Modifique su nombre:', max_length= 15, required=True)
    last_name= forms.CharField(label='Modifique su apellido:', max_length= 15, required=True)
    email = forms.EmailField  (label = 'Modifique su e-mail')
    image = forms.ImageField(label= 'Modifique su foto:', required=False)
    description= forms.CharField(label='Descripción:', max_length= 15, required=False)
    link= forms.CharField(label='Link:', max_length= 25, required=False)
    password1=forms.CharField(label='Modifique su contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'image', 'description', 'link']
        help_texts = {k:'' for k in fields} 

class pizza_form (forms.ModelForm):
    class Meta:
        model = pizza
        fields = '__all__'

class empanada_form (forms.ModelForm):
    class Meta:
        model = empanada
        fields = '__all__'

class bebida_form (forms.ModelForm):
    class Meta:
        model = bebida
        fields = '__all__'

class postre_form (forms.ModelForm):
    class Meta:
        model = postre
        fields = '__all__'

class portada_form (forms.ModelForm):
    class Meta:
        model = portada
        fields = '__all__'

class portada_secundaria_form (forms.ModelForm):
    class Meta:
        model = secundaria_portada
        fields = '__all__'

class portada_about_form (forms.ModelForm):
    class Meta:
        model = about_portada
        fields = '__all__'