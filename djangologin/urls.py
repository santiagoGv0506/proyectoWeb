"""
URL configuration for djangologin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('index/', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
    path('foro/', views.temas, name='temas'),
    
    path('nuevoTema/', views.nuevoTema, name='nuevoTema'),
    path('editar_tema/<int:tema_id>/', views.editarTema, name='editar_tema'),
    path('eliminar_tema/<int:tema_id>/', views.eliminarTema, name='eliminar_tema'),
    
]
