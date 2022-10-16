from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Folio, Quartet, Entry
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
        context["entries"] = Entry.objects.all()
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

class QuartetDetail(DetailView):
    model = Quartet
    template_name = "quartet_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folios"] = Folio.objects.all()
        # # context["folios"] = Folio.objects.get(pk=self.object.pk)
        context["quartets"] = Quartet.objects.all()
        context["entries"] = Entry.objects.all()
        return context

class QuartetCreate(CreateView):
    model = Quartet
    fields = ['name', 'folio']
    template_name = "new_quartet.html"
    
    def get_success_url(self):
        return reverse('folio_detail', kwargs={'pk': self.object.folio.pk})

class QuartetUpdate(UpdateView):
    model = Quartet
    fields = ['name']
    template_name = "quartet_update.html"
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.folio.pk, 'pk': self.object.pk})

class QuartetDelete(DeleteView):
    model = Quartet
    template_name = "quartet_delete_confirmation.html"
    
    def get_success_url(self):
        return reverse('folio_detail', kwargs={'pk': self.object.folio.pk})

class TextEntryCreate(CreateView):
    model = Entry
    fields = ['text', 'quartet']
    template_name = "new_text_entry.html"
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.quartet.folio.pk,'pk': self.object.quartet.pk})

class ImageEntryCreate(CreateView):
    model = Entry
    fields = ['image', 'annotate', 'quartet']
    template_name = "new_image_entry.html"
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.quartet.folio.pk,'pk': self.object.quartet.pk})

class EmbedEntryCreate(CreateView):
    model = Entry
    fields = ['embed', 'quartet']
    template_name = "new_embed_entry.html"
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.quartet.folio.pk,'pk': self.object.quartet.pk})

class VideoEntryCreate(CreateView):
    model = Entry
    fields = ['embed', 'annotate', 'quartet']
    template_name = "new_video_entry.html"
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.quartet.folio.pk,'pk': self.object.quartet.pk})