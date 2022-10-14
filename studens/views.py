from django.shortcuts import render

# Create your views here.

def studs(request):
    return render(request,'studens/studenshome.html')