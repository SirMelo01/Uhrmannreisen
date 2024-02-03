# myapp/middleware.py
from django.http import HttpResponsePermanentRedirect


class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().partition(":")[0]
        if host == "www.uhrmann-reisen.de":
            return HttpResponsePermanentRedirect("https://uhrmann-reisen.de" + request.path)
        else:
            return self.get_response(request)