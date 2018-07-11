from django.shortcuts import render,reverse
from django.http import HttpResponse

# Create your views here.
def sayhello(request):
    return HttpResponse('sayhello')

def say(request):
    return HttpResponse('say')


def index(request):
    url=reverse("users:index")
    print(url)

    return HttpResponse('hello django')
