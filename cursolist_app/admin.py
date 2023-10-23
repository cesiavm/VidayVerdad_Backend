from django.contrib import admin
from cursolist_app.models import Curso,Nivel,Trimestre,Grado,Turno
# Register your models here.
admin.site.register(Curso)
admin.site.register(Trimestre)
admin.site.register(Grado)
admin.site.register(Nivel)
admin.site.register(Turno)