from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Folio, Quartet, Entry
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

@method_decorator(login_required, name='dispatch')
class FolioList(TemplateView):
    template_name = "folios.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["folios"] = Folio.objects.filter(name__icontains=name, user=self.request.user)
        else:
            context["folios"] = Folio.objects.filter(user=self.request.user)
        return context

class FolioCreate(CreateView):
    model = Folio
    fields = ['name']
    template_name = "new_folio.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FolioCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('folio_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class QuartetDetail(DetailView):
    model = Quartet
    template_name = "quartet_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folios"] = Folio.objects.all()
        context["quartets"] = Quartet.objects.all()
        context["entries"] = Entry.objects.all()
        return context

class QuartetCreate(LoginRequiredMixin, CreateView):
    model = Quartet
    fields = ['name', 'folio']
    template_name = "new_quartet.html"


    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['folio'].queryset = form.fields['folio'].queryset.filter(user=self.request.user.id)
        return form
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuartetCreate, self).form_valid(form)

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

class TextEntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['text', 'quartet']
    template_name = "new_text_entry.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['quartet'].queryset = form.fields['quartet'].queryset.filter(user=self.request.user.id)
        return form
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.quartet.folio.pk,'pk': self.object.quartet.pk})

class ImageEntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['image', 'annotate', 'quartet']
    template_name = "new_image_entry.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['quartet'].queryset = form.fields['quartet'].queryset.filter(user=self.request.user.id)
        return form
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.quartet.folio.pk,'pk': self.object.quartet.pk})

class EmbedEntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['embed', 'quartet']
    template_name = "new_embed_entry.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['quartet'].queryset = form.fields['quartet'].queryset.filter(user=self.request.user.id)
        return form
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.quartet.folio.pk,'pk': self.object.quartet.pk})

class VideoEntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['embed', 'annotate', 'quartet']
    template_name = "new_video_entry.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['quartet'].queryset = form.fields['quartet'].queryset.filter(user=self.request.user.id)
        return form
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.quartet.folio.pk,'pk': self.object.quartet.pk})

class EntryDelete(DeleteView):
    model = Entry
    template_name = "entry_delete_confirmation.html"
    
    def get_success_url(self):
        return reverse('quartet_detail', kwargs={'folio_pk': self.object.quartet.folio.pk, 'pk': self.object.quartet.pk})

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("folios")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
