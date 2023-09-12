from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('clientes/lista',views.lista, name='lista'),
    path('clientes/crear', views.crear, name='crear')


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #Para que muestre las imagenes


