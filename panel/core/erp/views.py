from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

def test(request):
    data = {
        'name':'Gabriel',
    }
    return render(request,'index.html',data)
