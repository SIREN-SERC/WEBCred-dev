import requests
import lxml.html


def preprocess(get_response):
    def middleware(request):
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
