
# Este es el archivo de configuración de URLs para el proyecto, rutas madre.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('integracion/', include('apps.integracion_compuesta.urls')),
    path('newton/', include('apps.newton_raphson.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
]

# Esto es necesario para servir archivos estáticos y de medios durante el desarrollo.

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)