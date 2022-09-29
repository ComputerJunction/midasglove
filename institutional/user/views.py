from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from json import dumps

from .models import PCikAndCusip,PCikmap

def user(request):

    context = PCikmap()



    return render(request, './html/user.html', {"context":context})


def cik(request):

    context = PCikAndCusip.return_json()

    return render(request, './html/cik.html', {"context":context})

