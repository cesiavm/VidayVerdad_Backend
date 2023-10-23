from django.shortcuts import get_object_or_404
from cursolist_app.models import Curso,Grado,Turno
from cursolist_app.api.serializers import CursoSerializer,GradoSerializer,TurnoSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets


class TurnoList(generics.ListCreateAPIView):
     queryset=Turno.objects.all()
     serializer_class=TurnoSerializer

class TurnoCursoList(generics.ListAPIView):
    serializer_class=CursoSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Curso.objects.filter(grado=pk)
    
class TurnoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Turno.objects.all()
    serializer_class=TurnoSerializer

class CursoVS(viewsets.ModelViewSet):
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer

# class CursoCreate(generics.CreateAPIView):
#      queryset=Curso.objects.all()
#      serializer_class=CursoSerializer
     
# class CursoList(generics.ListCreateAPIView):
#      queryset=Curso.objects.all()
#      serializer_class=CursoSerializer
    
    
# class CursoListAV(APIView):
    
#     def get(self, request):
#         cursos=Curso.objects.all()
#         serializer=CursoSerializer(cursos,many=True,context={'request':request})
#         return Response(serializer.data)        

#     def post(self, request):
#         serializer=CursoSerializer(data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
# class CursoDetalleAV(APIView):
#     def get(self, request,pk):
#         try:
#             curso=Curso.objects.get(pk=pk)
#         except Curso.DoesNotExist:
#             return Response({'error':'Curso no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer= CursoSerializer(curso,context={'request': request})
#         return Response(serializer.data)
    
#     def put(self, request,pk):
#         try:
#             curso=Curso.objects.get(pk=pk)
#         except Curso.DoesNotExist:
#             return Response({'error':'Curso no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer=CursoSerializer(curso,data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,pk):
#         try:
#             curso=Curso.objects.get(pk=pk)
#         except Curso.DoesNotExist:
#             return Response({'error':'Curso no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
#         curso.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET','POST']) 
# def curso_list(request):
#     if request.method=='GET':
#         cursos=Curso.objects.all()
#         serializer=CursoSerializer(cursos,many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         de_serializer=CursoSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)
        
# @api_view(['GET','PUT','DELETE'])
# def curso_detalle(request,pk):
#     if request.method=='GET':
#         try:
#             curso=Curso.objects.get(pk=pk)
#             serializer=CursoSerializer(curso)
#             return Response(serializer.data)
#         except Curso.DoesNotExist:
#             return Response({'Error':'el curso no existe'},status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='PUT':
#         curso=Curso.objects.get(pk=pk)
#         de_serializer=CursoSerializer(curso,data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method=='DELETE':
#         try:
#             curso=Curso.objects.get(pk=pk)
#             curso.delete()
#         except Curso.DoesNotExist:
#             return Response({'Error':'El Curso no existe'},status=status.HTTP_404_NOT_FOUND)
#         return Response (status=status.HTTP_204_NO_CONTENT)
        