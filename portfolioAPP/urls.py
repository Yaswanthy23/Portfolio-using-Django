from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path("projects/",views.projects,name="projects"),
    path('info/', views.info, name="info"),

]