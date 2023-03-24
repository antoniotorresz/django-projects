from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm

# Create your views here.
class NewDepartamentoView(FormView):
    template_name = 'departamentos/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        return super(NewDepartamentoForm, self).form_valid(form)