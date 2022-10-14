from tkinter.messagebox import RETRY
from django.shortcuts import render


def HomePage(request):
    
    return render(request, 'index.html')