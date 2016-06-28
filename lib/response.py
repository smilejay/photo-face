'''
Created on June 28, 2016

@author: Jay <smile665@gmail.com>
'''

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


if __name__ == '__main__':
    print JSONResponse(data={'name': 'Jay'}, status=200)
