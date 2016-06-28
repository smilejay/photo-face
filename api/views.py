# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse
from lib.utility import save_file
from .forms import UploadFileForm


@csrf_exempt
def upload(request):
    ''' demo for uploading a file'''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            save_file(request.FILES['file'], 'img_orig/1.jpg')
            return JSONResponse(data='upload ok', status=200)
        else:
            return JSONResponse(data=form.errors, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP GET method.'},
            status=200)


@csrf_exempt
def detect_face(request):
    '''
    @summary: get songs by category id.
    '''
    if request.method == 'GET':
        req = Request(request)
        return JSONResponse(data='ok', status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP GET method.'},
            status=200)
