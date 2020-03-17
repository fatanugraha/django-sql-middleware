from django.shortcuts import render
from django.http import HttpResponse

from .globals import store, clear_request, remove_request


def index(request):
    return render(request, "sqlmiddleware/index.html", {'store': store})


def detail(request, id):
    if request.method == "DELETE":
        remove_request(id)
        return HttpResponse(status=204)
    elif request.method == "GET":
        return render(request, "sqlmiddleware/detail.html", {'data': store[str(id)]})


def clear(request):
    clear_request()
    return HttpResponse(status=204)
