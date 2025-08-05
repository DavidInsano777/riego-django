from django.contrib import admin
from .models import Lectura
# Register your models here.
@admin.register(Lectura)
class LecturaAdmin(admin.ModelAdmin):
    list_display = ('humedad', 'riego', 'fecha')
    list_filter = ('riego',)
    ordering = ('-fecha',)