import requests
import lxml.html
from django.urls import resolve

from webcred import views


def preprocess(get_response):

    def middleware(request):

        if resolve(request.path).func != views.assess:
            return get_response(request)

        url = request.POST.get('url')
        response = requests.get(url)
        document = lxml.html.fromstring(response.text)

        request.data = {
            'url': url,
            'res': response,
            'doc': document
        }

        return get_response(request)

    return middleware
