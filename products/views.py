from django.views.generic import TemplateView
from django.shortcuts import render

class ProductView(TemplateView):
    template_name = 'products/products.html'

    def product(self, request):
        return render(request, self.template_name)

