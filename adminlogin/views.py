from django.shortcuts import render

# Create your views here.
def adminlogin(request):
    return render(request, 'adminlogin/adminlogin.html')
