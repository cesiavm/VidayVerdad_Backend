from django.db import models
#from estudiante_app.detalles_models import DetalleCentroSalud,DetalleAccesoInternet,DetalleMes,DetalleRazonAbandono
from django.apps import apps

class Estudiante(models.Model):
    Sexo_ = [
        (True, 'Hombre'),
        (False, 'Mujer')
    ]
    id_estudiante = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    foto = models.CharField(max_length=255,  blank=True)
    ci = models.CharField(max_length=30, unique=True)
    complemento = models.CharField(max_length=10, blank=True)
    expedido = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    sexo = models.BooleanField(choices=Sexo_)
    numero_rude = models.BigIntegerField(unique=True)
    estado_pago = models.BooleanField(default=True)
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'estudiante' 
    def __str__(self):
        return self.nombres
    
class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'pais' 
    def __str__(self):
        return self.nombre_pais

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=50, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE,db_column='pais', to_field='id_pais',
                            )
   
    class Meta:
        db_table = 'departamento' 
    def __str__(self):
        return self.nombre_departamento

class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=50, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,db_column='departamento', to_field='id_departamento')
    class Meta:
        db_table = 'provincia' 
    def __str__(self):
        return self.nombre_provincia

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nombre_municipio = models.CharField(max_length=50, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,db_column='departamento', to_field='id_departamento')
    class Meta:
        db_table = 'municipio' 
    def __str__(self):
        return self.nombre_municipio

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    nombre_localidad = models.CharField(max_length=50, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,db_column='departamento', to_field='id_departamento')
    class Meta:
        db_table = 'localidad' 
    def __str__(self):
        return self.nombre_localidad
    
class TipoDiscapacidad(models.Model):
    id_tipo_discapacidad= models.AutoField(primary_key=True)
    tipo_discapacidad = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'tipo_discapacidad' 
    def __str__(self):
        return self.tipo_discapacidad

class GradoDiscapacidad(models.Model):
    id_grado_discapacidad= models.AutoField(primary_key=True)
    grado_discapacidad = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'grado_discapacidad' 
    def __str__(self):
        return self.grado_discapacidad

class Idioma(models.Model):
    id_idioma= models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'idioma' 
    def __str__(self):
        return self.idioma

class NacionPuebloIndigena(models.Model):
    id_nacion_pueblo_indigena= models.AutoField(primary_key=True)
    nacion_pueblo_indigena = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'nacion_pueblo_indigena' 
    def __str__(self):
        return self.nacion_pueblo_indigena

class CentroSalud(models.Model):
    id_centro_salud= models.AutoField(primary_key=True)
    centro_salud = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'centro_salud' 
    def __str__(self):
        return self.centro_salud
    
class FrecuenciaSalud(models.Model):
    id_frecuencia_salud= models.AutoField(primary_key=True)
    frecuencia_salud = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'frecuencia_salud' 
    def __str__(self):
        return self.frecuencia_salud
    
class Vivienda(models.Model):
    id_vivienda= models.AutoField(primary_key=True)
    vivienda = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'vivienda' 
    def __str__(self):
        return self.vivienda

class AccesoInternet(models.Model):
    id_acceso_internet= models.AutoField(primary_key=True)
    acceso_internet = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'acceso_internet' 
    def __str__(self):
        return self.acceso_internet

class FrecuenciaInternet(models.Model):
    id_frecuencia_internet= models.AutoField(primary_key=True)
    frecuencia_internet = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'frecuencia_internet' 
    def __str__(self):
        return self.frecuencia_internet

class ActividadTrabajo(models.Model):
    id_actividad_trabajo= models.AutoField(primary_key=True)
    actividad_trabajo = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'actividad_trabajo' 
    def __str__(self):
        return self.actividad_trabajo

class FrecuenciaTrabajo(models.Model):
    id_frecuencia_trabajo= models.AutoField(primary_key=True)
    frecuencia_trabajo = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'frecuencia_trabajo' 
    def __str__(self):
        return self.frecuencia_trabajo

class TurnoTrabajo(models.Model):
    id_turno_trabajo= models.AutoField(primary_key=True)
    turno_trabajo = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'turno_trabajo' 
    def __str__(self):
        return self.turno_trabajo

class MedioTransporte(models.Model):
    id_medio_transporte= models.AutoField(primary_key=True)
    medio_transporte = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'medio_transporte' 
    def __str__(self):
        return self.medio_transporte 
    
class TiempoTransporte(models.Model):
    id_tiempo_transporte= models.AutoField(primary_key=True)
    tiempo_transporte = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'tiempo_transporte' 
    def __str__(self):
        return self.tiempo_transporte
    
class Mes(models.Model):
    id= models.AutoField(primary_key=True)
    nombre_mes = models.CharField(max_length=100, blank=True)
    numero_mes = models.IntegerField()
    class Meta:
        db_table = 'mes' 
    def __str__(self):
        return str(self.numero_mes)
    
class RazonAbandono(models.Model):
    id_razon_abandono= models.AutoField(primary_key=True)
    razon_abandono = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'razon_abandono' 
    def __str__(self):
        return self.razon_abandono
    
class RelacionFamiliar(models.Model):
    id_relacion_familiar= models.AutoField(primary_key=True)
    relacion_familiar = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'relacion_familiar' 
    def __str__(self):
        return self.relacion_familiar
    
    from django.db import models

class RegistroRude(models.Model):
    
    id_registro_rude= models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,db_column='estudiante', to_field='id_estudiante')
    lugar_de_nacimiento_pais = models.ForeignKey(Pais, on_delete=models.CASCADE,db_column='lugar_de_nacimiento_pais', to_field='id_pais')
    lugar_de_nacimiento_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,db_column='lugar_de_nacimiento_departamento', to_field='id_departamento', related_name='lugar_de_nacimiento_departamento')
    lugar_de_nacimiento_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE,db_column='lugar_de_nacimiento_provincia', to_field='id_provincia', related_name='lugar_de_nacimiento_provincia')
    lugar_de_nacimiento_localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE,db_column='lugar_de_nacimiento_localidad', to_field='id_localidad', related_name='lugar_de_nacimiento_localidad')
    numero_oficialia = models.IntegerField()
    numero_libro = models.IntegerField()
    numero_partida = models.IntegerField()
    numero_folio = models.IntegerField()
    discapacidad = models.BooleanField()
    numero_registro_discapacidad = models.IntegerField(null=True, blank=True)
    tipo_discapacidad = models.ForeignKey(TipoDiscapacidad, on_delete=models.CASCADE,db_column='tipo_discapacidad', to_field='id_tipo_discapacidad', null=True, blank=True)
    grado_discapacidad = models.ForeignKey(GradoDiscapacidad, on_delete=models.CASCADE,db_column='grado_discapacidad', to_field='id_grado_discapacidad', null=True, blank=True)
    direccion_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,db_column='direccion_departamento', to_field='id_departamento', related_name='direccion_departamento')
    direccion_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE,db_column='direccion_provincia', to_field='id_provincia', related_name='direccion_provincia')
    direccion_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE,db_column='direccion_municipio', to_field='id_municipio', related_name='direccion_provincia')
    direccion_localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE,db_column='direccion_localidad', to_field='id_localidad', related_name='direccion_provincia')
    zona_villa = models.CharField(max_length=100)
    avenida_calle = models.CharField(max_length=150)
    numero_vivienda = models.IntegerField()
    telefono_fijo = models.IntegerField()
    celular_contacto = models.IntegerField()
    idioma_niñez = models.ForeignKey(Idioma, on_delete=models.CASCADE,db_column='idioma_niñez', to_field='id_idioma', related_name='idioma_niñez')
    idioma_actual = models.ForeignKey(Idioma, on_delete=models.CASCADE,db_column='idioma_actual', to_field='id_idioma', related_name='idioma_actual')
    nacion_pueblo_indigena = models.ForeignKey(NacionPuebloIndigena, on_delete=models.CASCADE,db_column='nacion_pueblo_indigena', to_field='id_nacion_pueblo_indigena', related_name='nacion_pueblo_indigena_registro')
    centro_salud = models.BooleanField()
    frecuencia_salud = models.ForeignKey(FrecuenciaSalud, on_delete=models.CASCADE,db_column='frecuencia_salud', to_field='id_frecuencia_salud')
    seguro_salud = models.BooleanField()
    detalle_centro_salud = models.ManyToManyField(CentroSalud,through='DetalleCentroSalud')
    acceso_agua = models.BooleanField()
    acceso_baño = models.BooleanField()
    acceso_red_alcantarilla = models.BooleanField()
    acceso_energia_electrica = models.BooleanField()
    acceso_servicio_basura = models.BooleanField()
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE,db_column='vivienda', to_field='id_vivienda')
    frecuencia_internet = models.ForeignKey(FrecuenciaInternet, on_delete=models.CASCADE,db_column='frecuencia_internet', to_field='id_frecuencia_internet')
    detalle_acceso_internet = models.ManyToManyField(AccesoInternet,through='DetalleAccesoInternet')
    trabajo = models.BooleanField()
    detalle_mes = models.ManyToManyField(Mes,through='DetalleMes')
    actividad_trabajo = models.ForeignKey(ActividadTrabajo, on_delete=models.CASCADE,db_column='actividad_trabajo', to_field='id_actividad_trabajo')
    otro_trabajo = models.CharField(max_length=100, null=True, blank=True)
    detalle_turno_trabajo= models.ManyToManyField(TurnoTrabajo,through='DetalleTurnoTrabajo')
    frecuencia_trabajo = models.ForeignKey(FrecuenciaTrabajo, on_delete=models.CASCADE,db_column='frecuencia_trabajo', to_field='id_frecuencia_trabajo')
    pago = models.BooleanField()
    pago_tipo = [
        (True, 'En dinero'),
        (False, 'En Especie')
    ]
    tipo_pago = models.BooleanField(choices=pago_tipo)
    medio_transporte = models.ForeignKey(MedioTransporte, on_delete=models.CASCADE,db_column='medio_transporte', to_field='id_medio_transporte')
    otro_medio_transporte = models.CharField(max_length=100, null=True, blank=True)
    tiempo_transporte = models.ForeignKey(TiempoTransporte, on_delete=models.CASCADE,db_column='tiempo_transporte', to_field='id_tiempo_transporte')
    abandono_gestion_pasada = models.BooleanField()
    razon_abadono= models.ManyToManyField(RazonAbandono,through='DetalleRazonAbandono' )
    relacion_familiar = models.ForeignKey(RelacionFamiliar, on_delete=models.CASCADE,db_column='relacion_familiar', to_field='id_relacion_familiar')
    

    class Meta:
        db_table = 'registro_rude' 
    def __str__(self):
        return f'Registro Rude: {self.id_registro_rude}'
    
class DetalleCentroSalud(models.Model):
    id_detalle_centro_salud= models.AutoField(primary_key=True)
    registro_rude = models.ForeignKey(RegistroRude, on_delete=models.CASCADE,db_column='registro_rude', to_field='id_registro_rude')
    centro_salud = models.ForeignKey(CentroSalud, on_delete=models.CASCADE,db_column='centro_salud', to_field='id_centro_salud')
    class Meta:
        db_table = 'detalle_centro_salud' 

    

class DetalleAccesoInternet(models.Model):
    id_detalle_acceso_internet= models.AutoField(primary_key=True)
    registro_rude = models.ForeignKey(RegistroRude, on_delete=models.CASCADE,db_column='registro_rude', to_field='id_registro_rude')
    acceso_internet= models.ForeignKey(AccesoInternet, on_delete=models.CASCADE,db_column='acceso_internet', to_field='id_acceso_internet')
    class Meta:
        db_table = 'detalle_acceso_internet' 
    

class DetalleMes(models.Model):
    id_detalle_mes= models.AutoField(primary_key=True)
    registro_rude = models.ForeignKey(RegistroRude, on_delete=models.CASCADE,db_column='registro_rude', to_field='id_registro_rude')
    mes= models.ForeignKey(Mes, on_delete=models.CASCADE,db_column='mes')
    class Meta:
        db_table = 'detalle_mes'
    


class DetalleRazonAbandono(models.Model):
    id_detalle_razon_abandono= models.AutoField(primary_key=True)
    registro_rude = models.ForeignKey(RegistroRude, on_delete=models.CASCADE,db_column='registro_rude', to_field='id_registro_rude')
    razon_abandono= models.ForeignKey(RazonAbandono, on_delete=models.CASCADE,db_column='razon_abandono', to_field='id_razon_abandono')
    class Meta:
        db_table = 'detalle_razon_abandono' 
#     pass

class DetalleTurnoTrabajo(models.Model):
    id_detalle_turno_trabajo= models.AutoField(primary_key=True)
    registro_rude = models.ForeignKey(RegistroRude, on_delete=models.CASCADE,db_column='registro_rude', to_field='id_registro_rude')
    turno_trabajo= models.ForeignKey(TurnoTrabajo, on_delete=models.CASCADE,db_column='turno_trabajo', to_field='id_turno_trabajo')
    class Meta:
        db_table = 'detalle_turno_trabajo'