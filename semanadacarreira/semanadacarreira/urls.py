from django.contrib import admin
from django.urls import path
from .views import view_prof, view_aluno
import core.templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_prof, name='ProfForm'),
    path('alunos', view_aluno, name='ProfForm'),
]