from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from basic_app import models

# Create your views here.

class CBView(View):
    def get(self, request):
        return HttpResponse("Class based views are cool!")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'INJECTION!'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
