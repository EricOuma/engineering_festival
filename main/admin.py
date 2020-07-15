from django.contrib import admin
from main.models import Speaker, Program, SummitDay, Sponsor
from django.contrib.admin import AdminSite
from django.urls import path
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


admin.site.site_header = 'ENGINEERING FESTIVAL DASHBOARD'
admin.site.index_title = 'FESTIVAL ADMIN'

# Register your models here.


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(SummitDay)
class SummitDayAdmin(admin.ModelAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'speaker', 'start_time', 'end_time', 'venue')



@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass