from django.urls import path

from appcoder.views import *

urlpatterns = [
    path ('',inicio, name="inicio"),
    #path('cursos', cursos, name="cursos"),
    #path('estudiantes',estudiantes, name= "estudiantes"),
    #path('profesores', profesores, name= "profesores"),
    #path('entregables', entregables, name= "entregables"),
    #path('cursoFormulario',cursoFormulario,name="CursoFormulario"),
    #path('form-con-api', form_con_api, name="FormConApi"),    
    #path('buscar-form-con-api', buscar_form_con_api, name="Buscar_Form_Con_Api"), 
    #path('profesorFormulario', profesorFormulario, name="ProfesorFormulario"), 
    #path('lista/', CursoListView.as_view(), name = "ListarCursos"),
    path('cursos/lista/', CursoListView.as_view(), name = "ListaCursos"),
    path('cursos/nuevo/', CursoCreateView.as_view(), name = "NuevoCurso"),
    path('cursos/<pk>/', CursoDetailView.as_view(), name = "DetalleCurso"),
    path('cursos/<pk>/editar', CursoUpdateViuew.as_view(), name = "EditarCurso"),
    path('cursos/<pk>/borrar', CursoDetailView.as_view(), name = "BorrarCurso"),
]


