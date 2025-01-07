from django.shortcuts import render

# Create your views here.
def firstfunction(request):
    return render(request,'first.html')
