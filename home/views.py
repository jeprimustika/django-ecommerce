from django.views.generic import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'home/index.html'
    
    def home(self, request):
        return render(request, self.template_name)