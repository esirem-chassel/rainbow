from django.http import HttpResponse
from django.shortcuts import render

from gen.models import Record

def index(request):
    res = ""
    rs = Record.objects.all()
    for r in rs:
        res += f"{r.src} ==({r.flavor})=> {r.res}\n" 
    return HttpResponse(res)

def add(request):
    return HttpResponse("OK")

def rm(request):
    return HttpResponse("OK")

def flavors(request):
    return HttpResponse("OK")

def addFlavor(request):
    return HttpResponse("OK")
