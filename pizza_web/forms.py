from django import forms
from pizza_web.models import pizza, empanada, bebida, postre
from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class User_registration_form (UserCreationForm):
    email = forms.EmailField  ()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:''for k in fields}



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