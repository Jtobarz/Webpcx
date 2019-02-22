from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()
 
app_name='Webpcx'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'Contacto$',views.Contacto, name='Contacto'),
    url(r'Servicios$',views.Servicios, name='Servicios'),
    url(r'Gracias$',views.Gracias, name='Gracias'),
    url(r'jovenes$',views.jovenes, name='jovenes'),
    url(r'nuevo$',views.nuevo, name='nuevo'),
    url(r'enviar$',views.enviar, name='enviar'),
    url(r'ingresar$',views.ingresar, name='ingresar'),
    url(r'Noticias$',views.Noticias, name='Noticias'),
    url(r'LogSec$',views.LogSec, name='LogSec'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
