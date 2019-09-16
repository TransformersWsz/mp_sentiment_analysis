from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Specification


def index(request):
    return JsonResponse({"name": "我是想"}, safe=False, json_dumps_params={'ensure_ascii': False})


def get_phone_list(request):
    specification_objects = Specification.objects
    if request.GET["search"] == "all":
        items = specification_objects.all()
    else:
        items = specification_objects.filter(name__contains=request.GET["search"])

    resp = {
        'code': 200,
        'msg': 'query success',
        'data': []
    }
    for each_phone in items[int(request.GET["offset"]):int(request.GET["limit"])]:
        d = model_to_dict(each_phone)
        resp["data"].append(d)

    return JsonResponse(resp, safe=False, json_dumps_params={'ensure_ascii': False})


def page_not_found(request):
    return render(request, "404.html")


def page_error(request):
    return render(request, "500.html")
