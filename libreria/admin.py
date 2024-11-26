from django.contrib import admin
from .models import Libro
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'descripcion']

    list_display = ['titulo', 'descripcion']
    list_filter = ('estado',)

admin.site.register(Libro, LibroAdmin)