# -*- coding: utf-8 -*-
from datetime import datetime
import random
from django.views.decorators.csrf import csrf_exempt
from lib.response import JSONResponse
from lib.utility import save_file, key_validation
from face import face
from .forms import UploadFileForm

orig_dir = 'img_orig'
face_dir = 'static/img_face'
out_dir = 'static/img_out'


@csrf_exempt
def upload(request):
    ''' demo for uploading a file'''
    if request.method == 'POST':
        key = request.POST.get('key', 'aa')
        if not key_validation(key):
            return JSONResponse({'status': 1, 'msg': 'key error.'}, status=200)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            out_filename = '%d.jpg' % int(10**8 * random.random())
            date_dir = datetime.now().strftime('%Y/%m/%d')
            out_file = '%s/%s/%s' % (out_dir, date_dir, out_filename)
            save_file(request.FILES['file'], out_file)
            return JSONResponse({'status':0, 'url': out_file}, status=200)
        else:
            return JSONResponse({'status': 1, 'msg': form.errors}, status=200)
    else:
        return JSONResponse({'msg': 'It only support HTTP POST method.',
                             'status': 1}, status=200)


@csrf_exempt
def detect_face(request):
    ''' upload a photo and extract the 1st face in the photo '''
    if request.method == 'POST':
        key = request.POST.get('key', 'aa')
        if not key_validation(key):
            return JSONResponse({'status': 1, 'msg': 'key error.'}, status=200)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            r_num = int(10**8 * random.random())
            orig_filename = '%d.jpg' % r_num
            face_filename = '%d_face.jpg' % r_num
            date_dir = datetime.now().strftime('%Y/%m/%d')
            orig_file = '%s/%s/%s' % (orig_dir, date_dir, orig_filename)
            face_file = '%s/%s/%s' % (face_dir, date_dir, face_filename)
            save_file(request.FILES['file'], orig_file)
            if face.extract_face(orig_file, face_file):
                return JSONResponse({'msg': 'can not detect face in the photo',
                                     'status': 1}, status=200)
            else:
                return JSONResponse({'url': face_file, 'status': 0}, status=200)
        else:
            return JSONResponse({'status': 1, 'msg': form.errors}, status=200)
    else:
        return JSONResponse({'msg': 'It only support HTTP POST method.',
                             'status': 1}, status=200)
