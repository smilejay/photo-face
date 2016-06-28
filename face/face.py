#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import cv2
import os

#frontalface_xml = '/tmp/haarcascade_frontalface_default.xml'
frontalface_xml = '/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'


def detect_object(image):
    '''检测图片，获取人脸在图片中的坐标'''
    ret = []
    face_cascade = cv2.CascadeClassifier(frontalface_xml)
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        ret.append((x-w*0.1, y-y*0.4, x+w*1.1, y+h*1.1))
    return ret


def extract_face(infile, outfile):
    '''在原图上截取第1个头像并保存为outfile'''
    faces = detect_object(infile)
    im = Image.open(infile)
    if faces:
        out_dir = os.path.dirname(os.path.abspath(outfile))
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        draw = ImageDraw.Draw(im)
        draw.rectangle(faces[0], outline=(255, 0, 0))
        im.crop(faces[0]).save(outfile)
    else:
        return 'Error: cannot detect faces on %s' % infile


if __name__ == '__main__':
    extract_face('/tmp/src/m-1.jpg', '/tmp/dest/m-1-face.jpg')
