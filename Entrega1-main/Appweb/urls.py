
from django.urls import path
from Appweb.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', mainpage, name = "Inicio"),
    path("comprar/",comprar, name = "ComprarCarta"),
    path("buscarCarta/",busquedaCarta, name = "BuscarCarta"),
    path("Resultado/",resultados, name= "ResultadoBusqueda"),
    #CRUD para la clase Carta
    path("carta/list/", ListaCartas.as_view(), name= "CartasLeer"),
    path("carta/<int:pk>/", DetalleCarta.as_view(), name= "CartaDetalle"),
    path("carta/crear/", CrearCarta.as_view(), name= "CartaCrear"),
    path("carta/editar/<int:pk>", ActualizarCarta.as_view(), name= "CartaEditar"),
    path("carta/eliminar/<int:pk>", BorrarCarta.as_view(), name= "CartaEliminar"),
    #Login
    path("login/",inicioSesion, name="Login"),
    path("registro/",registro, name="Singup"),
    path("logout/", LogoutView.as_view(template_name="Appweb/logout.html"), name="Logout"),
    path("editar/", editarUsuario , name="EditarUsuario"),
    path("perfil/", perfil , name="Perfil"),
    #avatar
    path("agregarav/", agregarAvatar, name="AgregarAvatar"),
    path("about/", aboutpage, name = "About"),

]
