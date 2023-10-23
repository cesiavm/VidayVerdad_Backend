from rest_framework import serializers
from estudiante_app.models import (Estudiante,RegistroRude)

    
class EstudianteSerializer(serializers.ModelSerializer):

    class Meta :
        model=Estudiante
        fields="__all__"
    
class RegistroRudeSerializer(serializers.ModelSerializer):
    class Meta :
        model=RegistroRude
        fields="__all__"

# class CursoSerializer(serializers.ModelSerializer):
#     grado = GradoSerializer()
#     turno = TurnoSerializer()
#     class Meta:
#         model=Curso
#         fields= ['grado', 'turno', 'capacidad_estudiantes', 'cantidad_estudiantes', 'cantidad_asignaturas', 'active']
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['grado'] = instance.grado.nombre_grado
#         representation['turno'] = instance.turno.nombre_turno
        
#         return representation