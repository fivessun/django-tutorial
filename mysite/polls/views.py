from django import http


def index(request):
    return http.HttpResponse("Hello, world. You're at the polls index.")
