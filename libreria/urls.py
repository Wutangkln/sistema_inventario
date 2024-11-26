from django.urls import path 
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('libros', views.libros, name='libros')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    