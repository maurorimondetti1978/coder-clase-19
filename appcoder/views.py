from django.shortcuts import render
from appcoder.models import Curso
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def inicio(request):
    return render(request, "appcoder/inicio.html")

class CursoListView(ListView):
    model=Curso
    context_object_name= "curso"
    template_namee = "appcoder/curso_lista.html"

class CursoDetailView(DetailView):
    model=Curso
    template_namee = "appcoder/curso_detalle.html"

class CursoCreateView(CreateView):
    model= Curso
    template_name= "appcoder/curso_crear.html"
    success_url= reverse_lazy('ListaCursos')
    fields=['nombre', 'camada']

class CursoUpdateViuew(UpdateView):
    model= Curso
    template_name="appcoder/curso_editar.html"
    success_url=reverse_lazy('ListaCursos')
    fields=['nombre', 'camada']

class CursoDeleteView(DeleteView):
    model = Curso
    template_name= "appcoder/curso_borrar.html"
    success_url=reverse_lazy('ListaCursos')

