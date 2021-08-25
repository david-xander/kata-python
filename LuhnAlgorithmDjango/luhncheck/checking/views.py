from django.shortcuts import render

def check_home(request):
    return render(request, 'checking.html')
