from django.urls import include, path
from app1 import views


urlpatterns = [
    path("inicio/", views.home, name="home"),
    path("servicios/", views.servicios, name="servicios"),
    path("blog/", views.blog, name="blog"),
    path("contactos/", views.contacto, name="contacto"),
    path("base", views.base, name="base"),
]
