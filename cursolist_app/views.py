# from django.shortcuts import render
# from cursolist_app.models import Curso
# from django.http import JsonResponse
# # Create your views here.

# def curso_list(request):
#     cursos=Curso.objects.all()
#     data={
#         'cursos':list(cursos.values())
#     }
#     return JsonResponse(data)

# def curso_detalle(request,pk):
#     # curso=Curso.objects.get(pk=pk)
  
#     data={
#         'Grado': curso.grado.nombre_grado,
#         'Turno': curso.turno.nombre_turno,
#         'Capacidad Estudiante':curso.capacidad_estudiantes,
#         'Cantidad Estudiantes': curso.cantidad_estudiantes,
#         'Cantidad Asignaturas':curso.cantidad_asignaturas
        
#     }
#     return JsonResponse(data)