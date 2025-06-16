from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('integracion/', include('apps.integracion_compuesta.urls')),
    path('newton/', include('apps.newton_raphson.urls')),
]