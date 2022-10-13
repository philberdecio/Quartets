from django.contrib import admin
from .models import Folio, Quartet, Entry
# Register your models here.

admin.site.register(Folio)
admin.site.register(Quartet)
admin.site.register(Entry)