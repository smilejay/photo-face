#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import cv
import os


def detect_object(image):
    '''检测图片，获取人脸在图片中的坐标'''
    grayscale = cv.CreateImage((image.width, image.height), 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)

    cascade = cv.Load(
        '/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    rect = cv.HaarDetectObjects(
        grayscale, cascade, cv.CreateMemStorage(),
        1.1, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (20, 20))

    result = []
    for r in rect:
        result.append((r[0][0]-r[0][2]*0.1,
                       r[0][1]-r[0][3]*0.1,
                       r[0][0]+r[0][2]*1.1,
                       r[0][1]+r[0][3]*1.1))

    return result


def extract_face(infile, outfile):
    '''在原图上截取第1个头像并保存为outfile'''
    image = cv.LoadImage(infile)
    if image:
        faces = detect_object(image)

    im = Image.open(infile)
    if faces:
        out_dir = os.path.dirname(os.path.abspath(outfile))
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        draw = ImageDraw.Draw(im)
        draw.rectangle(faces[0], outline=(255, 0, 0))
        im.crop(faces[0]).save(outfile)
    else:
        print 'Error: cannot detect faces on %s' % infile


if __name__ == '__main__':
    extract_face('/tmp/src/m-1.jpg', '/tmp/dest/m-1-face.jpg')
