from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.db.models import Q

# ______________________lista, creacion, detalle, actualizacion, borrar

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# __________________________login/registro

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# __________________________Mixins y Decorators

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request , 'aplicacion/base.html')

# _______________________________________________________________class_views_carpinteros

class CarpinteroList(LoginRequiredMixin, ListView):
    model = Carpinteros

class CarpinteroCreate(LoginRequiredMixin, CreateView):
    model = Carpinteros
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'precio']
    success_url = reverse_lazy('carpinteros')
 
class CarpinteroDetail(LoginRequiredMixin, DetailView):
    model = Carpinteros

class CarpinteroUpdate(LoginRequiredMixin, UpdateView):
    model = Carpinteros
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'precio']
    success_url = reverse_lazy('carpinteros')

class CarpinteroDelete(LoginRequiredMixin, DeleteView):
    model = Carpinteros
    success_url = reverse_lazy('carpinteros')

# _______________________________________________________________carpinteros busqueda por localidad
@ login_required
def buscarCarpinterosZona(request):
    return render(request, "carpinteros_list.html")

@ login_required
def buscar2(request):
    zona = request.GET.get('zona', '')  
    if zona:
        localidad = Carpinteros.objects.filter(Q(localidad__iexact=zona))
    else:
        localidad = Carpinteros.objects.all()
    return render(request,
                  "aplicacion/carpinteros_list.html",
                  {"zona": zona, "carpinteros_list": localidad})


# ________________________________________________________class_views_electricistas

class ElectricistasList(LoginRequiredMixin, ListView):
    model = Electricistas

class ElectricistasCreate(LoginRequiredMixin, CreateView):
    model = Electricistas
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'categoria', 'matricula', 'precio']
    success_url = reverse_lazy('electricistas')
 
class ElectricistasDetail(LoginRequiredMixin, DetailView):
    model = Electricistas

class ElectricistasUpdate(LoginRequiredMixin, UpdateView):
    model = Electricistas
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'categoria', 'matricula', 'precio']
    success_url = reverse_lazy('electricistas')

class ElectricistasDelete(LoginRequiredMixin, DeleteView):
    model = Electricistas
    success_url = reverse_lazy('electricistas')

# _______________________________________________________________electricistas busqueda por localidad
@ login_required
def buscarElectricistasZona(request):
    return render(request, "electricistas_list.html")


@ login_required
def buscar3(request):
    zona = request.GET.get('zona', '')  
    if zona:
        localidad = Electricistas.objects.filter(Q(localidad__iexact=zona))
    else:
        localidad = Electricistas.objects.all()
    return render(request,
                  "aplicacion/electricistas_list.html",
                  {"zona": zona, "electricistas_list": localidad})


# ________________________________________________________class_views_plomeros

class PlomerosList(LoginRequiredMixin, ListView):
    model = Plomeros

class PlomerosCreate(LoginRequiredMixin, CreateView):
    model = Plomeros
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'categoria', 'matricula', 'precio']
    success_url = reverse_lazy('plomeros')
 
class PlomerosDetail(LoginRequiredMixin, DetailView):
    model = Plomeros

class PlomerosUpdate(LoginRequiredMixin, UpdateView):
    model = Plomeros
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'categoria', 'matricula', 'precio']
    success_url = reverse_lazy('plomeros')

class PlomerosDelete(LoginRequiredMixin, DeleteView):
    model = Plomeros
    success_url = reverse_lazy('plomeros')

# _______________________________________________________________plomeros busqueda por localidad

@ login_required
def buscarPlomerosZona(request):
    return render(request, "plomeros_list.html")

@ login_required
def buscar4(request):
    zona = request.GET.get('zona', '')  
    if zona:
        localidad = Plomeros.objects.filter(Q(localidad__iexact=zona))
    else:
        localidad = Plomeros.objects.all()
    return render(request,
                  "aplicacion/plomeros_list.html",
                  {"zona": zona, "plomeros_list": localidad})


# ________________________________________________________class_views_gasistas

class GasistasList(LoginRequiredMixin, ListView):
    model = Gasistas

class GasistasCreate(LoginRequiredMixin, CreateView):
    model = Gasistas
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'categoria', 'matricula', 'precio']
    success_url = reverse_lazy('gasistas')
 
class GasistasDetail(LoginRequiredMixin, DetailView):
    model = Gasistas

class GasistasUpdate(LoginRequiredMixin, UpdateView):
    model = Gasistas
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'categoria', 'matricula', 'precio']
    success_url = reverse_lazy('gasistas')

class GasistasDelete(LoginRequiredMixin, DeleteView):
    model = Gasistas
    success_url = reverse_lazy('gasistas')

# _______________________________________________________________gasistas busqueda por localidad

@ login_required
def buscarGasistasZona(request):
    return render(request, "gasistas_list.html")

@ login_required
def buscar5(request):
    zona = request.GET.get('zona', '')  
    if zona:
        localidad = Gasistas.objects.filter(Q(localidad__iexact=zona))
    else:
        localidad = Gasistas.objects.all()
    return render(request,
                  "aplicacion/gasistas_list.html",
                  {"zona": zona, "gasistas_list": localidad})


# ________________________________________________________class_views_pintores

class PintoresList(LoginRequiredMixin, ListView):
    model = Pintores

class PintoresCreate(LoginRequiredMixin, CreateView):
    model = Pintores
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'precio']
    success_url = reverse_lazy('pintores')
 
class PintoresDetail(LoginRequiredMixin, DetailView):
    model = Pintores

class PintoresUpdate(LoginRequiredMixin, UpdateView):
    model = Pintores
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad', 'precio']
    success_url = reverse_lazy('pintores')

class PintoresDelete(LoginRequiredMixin, DeleteView):
    model = Pintores
    success_url = reverse_lazy('pintores')

# _______________________________________________________________pintores busqueda por localidad

@ login_required
def buscarPintoresZona(request):
    return render(request, "pintores_list.html")

@ login_required
def buscar6(request):
    zona = request.GET.get('zona', '')  
    if zona:
        localidad = Pintores.objects.filter(Q(localidad__iexact=zona))
    else:
        localidad = Pintores.objects.all()
    return render(request,
                  "aplicacion/pintores_list.html",
                  {"zona": zona, "pintores_list": localidad})

# _____________________________________________________________________login

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, 'aplicacion/base.html', {"mensaje":f"Bienvenido/a {usuario}"})
            else:
                return render(request, 'aplicacion/login.html', {"form":miForm, "mensaje":f"Datos invalidos"})
        else:
            return render(request, 'aplicacion/login.html', { "form":miForm, "mensaje":f"Datos invalidos"})
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})
    

# ________________________________________________________________________registro

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) 
        if form.is_valid(): 
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Gracias por Registrarte"})        
    else:
        form = RegistroUsuariosForm() 

    return render(request, "aplicacion/registro.html", {"form": form})    



# ______________________________________________________________________acerca de mi
@ login_required
def acercaDeMi(request):
    return render(request, 'aplicacion/acercaDeMi.html', {})

# ______________________________________________________________________Editar registro
@ login_required
def editarRegistro(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            nuevo_email = form.cleaned_data.get('email')
            nueva_contraseña = form.cleaned_data.get('password1')

            usuario.email = nuevo_email
            usuario.set_password(nueva_contraseña)
            usuario.save()

            user = authenticate(username=usuario.username, password=nueva_contraseña)
            if user is not None:
                login(request, user)

            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarRegistro.html", {'form': form, 'usuario': usuario.username})
        
# ______________________________________________________________________avatar

@login_required
def imagenAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: 
                avatarViejo[0].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/imagenAvatar.html", {'form': form})


