from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomePage(View):
    def get(self , request):
        return render(request , "page/home.html")
