from django.shortcuts import render
#
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView,
)

from .models  import Prueba
from .forms import PruebaForm
#vista generica mara mostrar exclusivamente un archibo html
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

#vista generica que se usa exclusivamente para listar algo (objetos o registros en una base de datos)
class PruebaListaView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros' #parametro para declarar una variable que hace referencia al queryset
    queryset = ['1', '10', '20', '30']
    
    
    
class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'
    
#ayuda a registrar algo o crear un registro sobre un modelo de base de datos para no utilizar 
#eladministrador de django sino un template personalizado
class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'