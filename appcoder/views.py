from django.shortcuts import render
from appcoder.models import Curso
from appcoder.forms import CursoFormulario


# Create your views here.
def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

    cursos= Curso.objects.all()

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")

def cursoFormulario(request):

    if request.method == 'POST':

            curso =  Curso(request.post['curso'],(request.post['camada']))

            curso.save()

            return render(request, "appcoder/inicio.html")

    return render(request, "appcoder/cursoFormulario.html")

def form_con_api(request):

      if request.method == "POST":

            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                 informacion = miFormulario.cleaned_data
                 curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                 curso.save()
                 return render(request, "appcoder/inicio.html")
      else:
                 miFormulario = CursoFormulario()

      return render(request, "appcoder/cursoFormulario.html", {"miFormulario": miFormulario})


