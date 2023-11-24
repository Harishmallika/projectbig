from django.shortcuts import render

# Create your views here.


def dhamini(request):
    return render(request,'dhamini.html')

def rathika(request):
    return render(request,'rathika.html' ) 
       
def yavaar(request):
    return render(request,'yavaar.html' ) 
