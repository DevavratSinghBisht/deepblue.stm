from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def summary(request):
    # TODO add summarization code
    return HttpResponse('summary hit')