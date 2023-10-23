from django.urls import path,include
from rest_framework.routers import DefaultRouter
from estudiante_app.api.views import EstudianteVS,RegistroRude

router=DefaultRouter()
router.register('estudiante',EstudianteVS,basename='estudiante')
urlpatterns = [
    path('',include(router.urls)),
    #path('registro_rude/<int:pk>',RegistroRude.as_view(), name='registrorude-detail'),
    path('registro_rude-create/<int:pk>',RegistroRude.as_view(), name='registrorude-create'),

]
