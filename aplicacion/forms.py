from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        help_texts = {k:"" for k in fields}    

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

     
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        help_texts = { k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)               