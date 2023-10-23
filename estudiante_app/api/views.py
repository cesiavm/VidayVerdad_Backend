from django.shortcuts import get_object_or_404
from estudiante_app.models import Estudiante,RegistroRude
from estudiante_app.api.serializers import EstudianteSerializer,RegistroRudeSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets


class EstudianteVS(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all()
    serializer_class=EstudianteSerializer
    
class RegistroRudeVS(viewsets.ModelViewSet):
    queryset=RegistroRude.objects.all()
    serializer_class=RegistroRudeSerializer
    
    
class RegistroRude(APIView):
     def post(self, request,pk):
       try:
            estudiante=Estudiante.objects.get(pk=pk)
       except Estudiante.DoesNotExist:
           return Response({'error':'Estudiante no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
       serializer=RegistroRudeSerializer(data=request.data,context={'request':request})
       if serializer.is_valid():
            serializer.validated_data['estudiante'] = estudiante
            serializer.save()
            return Response(serializer.data)
       else:
                 return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class TurnoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Turno.objects.all()
#     serializer_class=TurnoSerializer