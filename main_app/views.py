from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Folio, Quartet
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class FolioList(TemplateView):
    template_name = "folios.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folios"] = Folio.objects.all() 
        return context

class Quartets(TemplateView):
    template_name = "quartets.html"

class FolioCreate(CreateView):
    model = Folio
    fields = ['name']
    template_name = "new_folio.html"
    
    def get_success_url(self):
        return reverse('folio_detail', kwargs={'pk': self.object.pk})

class FolioDetail(DetailView):
    model =Folio
    template_name = "folio_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folios"] = Folio.objects.all()
        context["quartets"] = Quartet.objects.all()
        return context

class FolioUpdate(UpdateView):
    model = Folio
    fields = ['name']
    template_name = "folio_update.html"
    success_url = "/folios/"
    
    def get_success_url(self):
        return reverse('folio_detail', kwargs={'pk': self.object.pk})

class FolioDelete(DeleteView):
    model = Folio
    template_name = "folio_delete_confirmation.html"
    success_url = "/folios/"