from django.contrib import admin
from estudiante_app.models import (RegistroRude,Estudiante,Pais,Departamento,Provincia,
                                   Municipio,Localidad,TipoDiscapacidad,GradoDiscapacidad,Idioma,
                                   NacionPuebloIndigena,CentroSalud,FrecuenciaSalud,
                                   Vivienda,AccesoInternet,FrecuenciaInternet,ActividadTrabajo,
                                   FrecuenciaTrabajo,MedioTransporte,TiempoTransporte,
                                   Mes,RazonAbandono,RelacionFamiliar,TurnoTrabajo
                                   )
# Register your models here.
admin.site.register(RegistroRude)
admin.site.register(Estudiante)
admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Localidad)
admin.site.register(TipoDiscapacidad)
admin.site.register(GradoDiscapacidad)
admin.site.register(Idioma)
admin.site.register(NacionPuebloIndigena)
admin.site.register(CentroSalud)
admin.site.register(FrecuenciaSalud)
admin.site.register(Vivienda)
admin.site.register(AccesoInternet)
admin.site.register(FrecuenciaInternet)
admin.site.register(ActividadTrabajo)
admin.site.register(FrecuenciaTrabajo)
admin.site.register(TurnoTrabajo)
admin.site.register(MedioTransporte)
admin.site.register(TiempoTransporte)
admin.site.register(Mes)
admin.site.register(RazonAbandono)
admin.site.register(RelacionFamiliar)

