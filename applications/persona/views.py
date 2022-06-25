from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.test import LiveServerTestCase
from django.views.generic import ( 
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    
)
#models
from .models import Empleado
#forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """vista que carga la pag de nicio"""
    template_name = 'inicio.html'
    

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista
    
class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

class ListByAreaEmpleado(ListView):
    """ lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name=area
        )
        return lista 

#vista sobre buscador    
class ListEmpleadosByKword(ListView):
    """ lista empleado por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name= palabra_clave
        )
        return lista
    
class ListHabilidadesHempleados(ListView):
    template_name = 'persona/habilidades.html'
    paginate_by = 4
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=3)
        return empleado.Habilidades.all()
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detailempleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'informacion del empleado'
        return context




class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
    
    
    
    
class EmpleadoUpDateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'Habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*****metodo post*****')
        print('======')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        print('****metodo form_valid******')
        print('**********')
        return super(EmpleadoUpDateView, self).form_valid(form)
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')