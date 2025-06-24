from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroUsuarioForm
from django.contrib import messages

# Registro de usuario
# Esta vista maneja el registro de nuevos usuarios. Si el método es POST, se procesa
# el formulario con los datos enviados. Si el formulario es válido, se crea el usuario,
# se inicia sesión automáticamente y se redirige al usuario a la página principal.

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('core:home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/register.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('core:home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('core:home')

