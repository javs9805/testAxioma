from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Usuario
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from datetime import datetime

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("hola")
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']
            
            # Buscar el usuario por el Rut
            try:
                usuario = Usuario.objects.get(rut=rut)
                # Autenticar al usuario
                if usuario.estado != "Inactivo":
                    user = authenticate(request, username=usuario.user.username, password=password)
                    if user is not None:
                        usuario.intentos = 0
                        usuario.save()
                        login(request, user)
                        return redirect('dashboard')
                    else:
                        usuario.intentos = usuario.intentos + 1
                        if usuario.intentos == 3:
                            usuario.intentos = 0
                            usuario.estado = "Inactivo"
                        usuario.save()
                        return render(request, 'registration/login.html', {'form': form,'intentos':3-usuario.intentos})
                else:
                    return render(request, 'registration/login.html', {'form': form,'inactivo':True})


            except ObjectDoesNotExist:
                print("no existe")
                form = LoginForm()
                return render(request, 'registration/login.html', {'form': form,'noExiste':True})
                #usuario no existe
                        
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form})

@login_required
def dashboardView(request):
    user = Usuario.objects.filter(user=request.user).first()
    print(user)
    formato = "%d/%m/%Y %H:%M"  # Formato "dd/mm/aaaa hh:mm"
    fecha_formateada = datetime.now().strftime(formato)
    return render(request,"login/dashboard.html", {'user':user,'time':fecha_formateada})


def exitView(request):
    logout(request)
    return redirect("loginView")