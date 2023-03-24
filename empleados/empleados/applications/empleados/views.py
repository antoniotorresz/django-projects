from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empleado

'''
1- Lista todos los empleados de la empresa
2- Listar todos los empleados que pertenecen a un area de la empresa
3- Listar empleados por trabajo
4- Listar empleados por palabra clave
5- Listar empleado por habilidades
'''


# Create your views here.
class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado


class ListByAreaEmpleado(ListView):
    '''Lista empleados de un area'''
    template_name = 'empleados/list_by_area.html'

    def get_queryset(self):
        # usar valor desde la url
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(departamento__short_name=area)
        return lista


class ListEmpleadosByKw(ListView):
    template_name = 'empleados/by_kw.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        print('------', palabra_clave)
        lista = Empleado.objects.filter(first_name=palabra_clave)
        print(lista)
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_empleado = self.request.GET.get('id_empleado', '')
        empleado = Empleado.objects.get(id=id_empleado)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleados/detail_empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = 'empleados/success.html'


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleados/add.html'
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']  # construir campos en especifico
    # fields = ('__all__')#construir todos los campos
    success_url = reverse_lazy('empleado_app:correcto')

    def form_valid(self, form):
        # logica del proceso
        empleado = form.save(commit=False)  # estamos almacenando toda la informacion del formulario en la bd
        print(empleado)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'empleados/update.html'
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']  # construir campos en especifico
    success_url = reverse_lazy('empleado_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/delete.html'
    success_url = reverse_lazy('empleado_app:correcto')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object)
        self.object.delete()
        return HttpResponse(self.success_url)