from django.shortcuts import render
from django.http import HttpResponse 
import datetime
# Create your views here.

def main(request):
    print(123)
    now = datetime.datetime.now()
    context = {'message':'Django 很棒','today':now}
    return render(request, 'main/main.html', context)
    #return HttpResponse("123")

