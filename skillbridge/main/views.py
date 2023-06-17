from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import RegistroUsuariosForm, FormularioLogin

# Create your views here.

def index(request):
    return render(request, 'landing.html')

class UsuariosView(TemplateView):
    template_name = 'usuarios.html'
    
    def get(self, request):
        usuarios = User.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'usuarios.html', context)

class RegistroUsuariosView(View):
    def get(self, request):
        form = RegistroUsuariosForm()
        context = {'form': form}
        return render(request, 'registro_usuarios.html', context)
    def post(self, request):
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            try:
                usuario = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password1'],
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    email = request.POST['email']
                )
                usuario.save()
                # login(request, 'usuarios')
                return redirect('usuarios')
            except Exception:
                context = {'form': form, 'error': 'El nombre de usuario ya existe'}
                return render(request, 'registro_usuarios.html', context)
        else:
            context = {'form': form }
            return render(request, "registro_usuarios.html", context)

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        context = {'login_form': FormularioLogin()}
        return render(request, 'login.html', context)

    def post(self, request):
        usuario = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']   
        )
        if usuario is not None:
            login(request, usuario)
            return redirect('index_privado')
        else:
            context = {'error': 'Usuario no encontrado', 'login_form': FormularioLogin()}
            return render(request, 'login.html', context)

@method_decorator(login_required, name='dispatch')
class PrivateIndexView(TemplateView):
    template_name = 'index_privado.html'
    
    def get(self, request):
        return render(request, 'index_privado.html')

    def post(self, request):
        return render(request, 'index_privado.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')