from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings

from .services import ptxApi

def index(request):
    objPtxApi = ptxApi(ptxId = settings.PTX_ID, ptxKey = settings.PTX_KEY)
    return JsonResponse(
        objPtxApi.get('https://ptx.transportdata.tw/MOTC/' + request.get_full_path()),
        safe=False
    )