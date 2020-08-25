from django.shortcuts import render

# Create your views here.
'''
def hello(request):
    return render(request,"myapp/template/hello.html",{})

'''
from django.http import HttpResponse

def hello(request):
    text = """<h1>welcome to my myapp !</h1>"""
    return HttpResponse(text)


'''
from django.http import HttpResponse

def hello(request, number):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)
'''
