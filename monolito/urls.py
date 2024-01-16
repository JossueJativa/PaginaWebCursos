from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "api"

router = routers.DefaultRouter()
router.register('cursos', views.CursosViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]