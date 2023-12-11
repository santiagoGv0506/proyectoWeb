from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import TemaForo
from .forms import TemaForoForm

# Create your views here.


def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context,request))

def noticias(request):
    return render(request, 'noticias.html')

def foro(request):
    return render(request, 'foro.html')



def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Registar
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm, "Error": 'Ya existe el usuario.'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm, "Error": 'La contraseña no coinciden'
        })

def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'signinota=models.CharField(max_length=30)n.html',{
                'form':AuthenticationForm,
                'Error':'Usuario o contrasena incorrecto '
            })
        else:
            login(request, user)
            return redirect('index')
        
def temas(request):
    temas = TemaForo.objects.all()
    return render(request, 'foro.html', {'temas': temas})


def nuevoTema(request):
    if request.method == 'GET':
        return render(request, 'nuevo_tema.html', {'form': TemaForoForm()})
    else:
        try:
            form = TemaForoForm(request.POST)
            if form.is_valid():
                new_tema = form.save(commit=False)
                new_tema.autor = request.user
                new_tema.save()
                return redirect('temas')
            else:
                return render(request, 'nuevo_tema.html', {'form': form, 'Error': 'Ingrese datos válidos'})
        except ValueError:
            return render(request, 'nuevo_tema.html', {'form': TemaForoForm(), 'Error': 'Ingrese datos válidos'})
        


def eliminarTema(request, tema_id):
    temas = TemaForo.objects.filter(id=tema_id, autor=request.user)
    if temas.exists():
        temas.delete()
    return redirect('temas')

def editarTema(request, tema_id):
    tema = get_object_or_404(TemaForo, id=tema_id, autor=request.user)

    if request.method == 'POST':
        form = TemaForoForm(request.POST, instance=tema)
        if form.is_valid():
            form.save()
            return redirect('temas')
    else:
        form = TemaForoForm(instance=tema)

    return render(request, 'editarTema.html', {'form': form, 'tema': tema})