from django.db import models

# Create your models here.
class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=100)
    imagen = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'asignatura'

    def __str__(self):
        return self.nombre_asignatura