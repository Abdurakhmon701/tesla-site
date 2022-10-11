from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'index.html'

class DetailPageView(TemplateView):
	template_name = 'detail.html'

class DetailPageView2(TemplateView):
	template_name = 'detail2.html'

class DetailPageView3(TemplateView):
	template_name = 'detail3.html'
# Create your views here.
