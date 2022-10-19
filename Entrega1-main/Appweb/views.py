from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from Appweb.models import *
from Appweb.forms import *
from django.views.generic import  ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def mainpage(request):
    return render(request,"Appweb/principal.html")


def aboutpage(request):
    return render(request,"Appweb/about.html" )



#Es la view para el llamar el formulario de busqueda en BD de "cartas"
def busquedaCarta(request):

    return render(request,"Appweb/busqueda.html")

#La view para los resultados de la busqueda en la BD de cartas
def resultados(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        carta = Cartas.objects.filter(nombre__icontains=nombre)

        return render(request,"Appweb/resultados.html", {"carta":carta, "nombre":nombre })
    
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#Una view simple que represeta de forma simbolica la compra de una carta a la cual
#se le realiza una busqueda. No quise implementar un sistema completo para no rebuscarme
#y no terminar usando codigo hecho por terceros. La idea era implementar un sistema de carrito para agregar objetos y que queden a la espera de "comprar"
def comprar(request):

    return render(request, "Appweb/principal.html", {"mensaje":"Gracias por su compra"})

#CRUD para la clase Carta hecho con clases

class ListaCartas(LoginRequiredMixin,ListView):
    model = Cartas

class DetalleCarta(LoginRequiredMixin,DetailView):

    model = Cartas

class CrearCarta(LoginRequiredMixin,CreateView):

    model = Cartas
    success_url = "/Appweb/carta/list"
    fields = ["nombre","precio","imagen","stock","descripcion","artista","rareza","tipo","costo"]


class ActualizarCarta(LoginRequiredMixin,UpdateView):

    model = Cartas
    success_url = "/Appweb/carta/list"
    fields = ["nombre","precio","imagen","stock","descripcion","artista","rareza","tipo","costo"]

class BorrarCarta(LoginRequiredMixin,DeleteView):

    model = Cartas
    success_url = "/Appweb/carta/list"

#Sistema de login
def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = passw)

            if user:
                login(request, user)

                return render(request, "Appweb/principal.html", {"mensaje": f"Bienvenido {user}"})
        else:
            return render(request,"Appweb/principal.html",{"mensaje":"Error de inicio se sesion: Datos incorrectos"})
    else:
        form = AuthenticationForm()

    return render (request,"Appweb/login.html",{"formulario":form})

#Sistema de registro
def registro (request):

    if request.method == "POST":
        
        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Appweb/principal.html", {"mensaje":"Usuario creado."})
    else:
        form = UsuarioRegistro()

    return render(request, "Appweb/registro.html", {"formulario":form})

#Edicion de usuario
@login_required
def editarUsuario(request):
    
    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password = info["password1"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "Appweb/principal.html")
    else:

        form = FormularioEditar(initial={
            "email":usuario.email,"first_name":usuario.first_name,
            "last_name":usuario.last_name
        })
    
    return render(request, "Appweb/editarPerfil.html",{"formulario":form, "usuario":usuario})

#Agregar un avatar de usuario
@login_required
def agregarAvatar(request):

    if request.method=="POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen = form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "Appweb/principal.html")
    else:
        form = AvatarFormulario()
    
    return render(request, "Appweb/agregarAvatar.html", {"formulario":form})

@login_required
def perfil(request):
    usuario = request.user
    
    return render(request, "Appweb/Perfil.html",{"usuario":usuario})