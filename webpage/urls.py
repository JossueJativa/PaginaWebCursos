from django.urls import path
from . import views

app_name = "webpage"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("curso/<int:curso_id>", views.curso, name="curso"),
    path("cursos-personales", views.cursos_personales, name="cursos_personales"),
]