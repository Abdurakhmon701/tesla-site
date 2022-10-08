from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'index.html'
class DetailPageView(TemplateView):
	template_name = 'detail.html'
# Create your views here.
