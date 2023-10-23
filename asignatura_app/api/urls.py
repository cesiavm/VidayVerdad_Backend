from django.urls import path
# from cursolist_app.api.views import curso_list,curso_detalle
#from asignatura_app.api.views import AsignaturaListAV,AsignaturaDetalleAV
from asignatura_app.api.views import AsignaturaList,AsignaturaDetail,AsignaturaCreate
                                    

urlpatterns = [
   path('asignatura-create/',AsignaturaCreate.as_view(), name='asignatura-create'),
    path('asignatura/',AsignaturaList.as_view(),name='asignatura-list'),
    path('asignatura/<int:pk>',AsignaturaDetail.as_view(), name='asignatura-detail'),

]