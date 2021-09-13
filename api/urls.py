from django.urls import path
from django.urls.resolvers import URLPattern
from .views import dotaciones, insertar_dotacion, asignar_dotacion
urlpatterns = {
    path('dotacion/', dotaciones, name='dotaciones_list' ),
    path('insertar_dotacion/', insertar_dotacion, name='insertar_dotacion' ),
    path('asignar_dotacion/', asignar_dotacion, name='asignar_dotacion' ),
}