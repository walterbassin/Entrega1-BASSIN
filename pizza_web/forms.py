from django import forms
from pizza_web.models import pizza, empanada, bebida, postre

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