# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request, 'dashboard_staff.html')