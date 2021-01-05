#from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.


class Hello(View):
    def get(self, request):
        return HttpResponse('<h1>HEllo World This is from class BAsead views</h1>')


class HelloT(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Gova'
        context['city'] = 'Sathandlahalli'
        context['marks'] = 100
        context['subject'] = 'Python'
        return context
