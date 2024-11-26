from django.db import models

# Create your models here.
class Libro(models.Model):
    
    DISPONIBLE = 'Disponible'
    NO_DISPONIBLE = 'No Disponible'

    ESTADO_CHOICES = [
        (DISPONIBLE, 'Disponible'),
        (NO_DISPONIBLE, 'No disponible'),
    ]

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name ='Titulo')
    imagen = models.ImageField(upload_to='imagenes_upload/', verbose_name ='Imagen', null=True)
    descripcion = models.TextField(verbose_name ='Descipción', null=True)
    estado = models.CharField(max_length=20,choices=ESTADO_CHOICES,default=DISPONIBLE)

    def __str__(self):
        fila = 'Título: ' + self.titulo + '  |  ' + 'Descripción: ' + self.descripcion + '  |  ' + 'Estado' + self.estado
        return fila     
        
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    