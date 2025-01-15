from django.shortcuts import render

def show_hello(request):
    return render(request, 'index.html')