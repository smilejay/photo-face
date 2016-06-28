#!/bin/bash
# the setup script for CentOS 7.x
yum install -y gcc cmake
yum install -y zlib zlib-devel libjpeg-turbo libjpeg-turbo-devel freetype freetype-devel
yum install -y numpy opencv*
easy_install -i https://pypi.tuna.tsinghua.edu.cn/simple pip
pip install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install Django djangorestframework -i https://pypi.tuna.tsinghua.edu.cn/simple
