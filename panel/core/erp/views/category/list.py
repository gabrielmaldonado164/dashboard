from django.shortcuts import render

def lista(request):
    data = {

        'title':' List category',

    }
    return render(request, 'category/list.html', data )