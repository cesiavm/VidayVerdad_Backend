from asignatura_app.models import Asignatura
from asignatura_app.api.serializers import AsignaturaSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins 

class AsignaturaCreate(generics.CreateAPIView):
     queryset=Asignatura.objects.all()
     serializer_class=AsignaturaSerializer

class AsignaturaList(generics.ListCreateAPIView):
     queryset=Asignatura.objects.all()
     serializer_class=AsignaturaSerializer

class AsignaturaDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset=Asignatura.objects.all()
     serializer_class=AsignaturaSerializer


# class AsignaturaList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Asignatura.objects.all()
#     serializer_class=AsignaturaSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class AsignaturaDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset=Asignatura.objects.all()
#     serializer_class=AsignaturaSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class AsignaturaListAV(APIView):
    
#     def get(self, request):
#         asignatura=Asignatura.objects.all()
#         serializer=AsignaturaSerializer(asignatura,many=True,context={'request':request})
#         return Response(serializer.data)        

#     def post(self, request):
#         serializer=AsignaturaSerializer(data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
# class AsignaturaDetalleAV(APIView):
#     def get(self, request,pk):
#         try:
#             asignatura=Asignatura.objects.get(pk=pk)
#         except Asignatura.DoesNotExist:
#             return Response({'error':'Curso no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer= AsignaturaSerializer(asignatura,context={'request': request})
#         return Response(serializer.data)
    
#     def put(self, request,pk):
#         try:
#             asignatura=Asignatura.objects.get(pk=pk)
#         except Asignatura.DoesNotExist:
#             return Response({'error':'Curso no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer=AsignaturaSerializer(asignatura,data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,pk):
#         try:
#             asignatura=Asignatura.objects.get(pk=pk)
#         except Asignatura.DoesNotExist:
#             return Response({'error':'Curso no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
#         asignatura.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
