from rest_framework import serializers
from asignatura_app.models import Asignatura


    
class AsignaturaSerializer(serializers.ModelSerializer):

    class Meta :
        model=Asignatura
        fields=['nombre_asignatura','imagen']
    