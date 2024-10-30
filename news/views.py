from django.shortcuts import render


# Create your views here.

def index(request):
    
    return render(request, 'index.html',context={'name':'Rohit'})


def about(request):
    data=[
        {'name':'Rohit','email':'rohita@gmail.com'},
        {'name':'laxmi','email':'laxmi@gmail.com'},
    ]

    data = {
        'userData':data
    }
    return render(request, 'about.html',data)
