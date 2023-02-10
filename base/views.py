from django.shortcuts import render

rooms = [
    {'id':1, 'name':'Lets learn PHP'},
    {'id':2, 'name':'Lets learn Python'},
    {'id':3, 'name':'Lets learn Golang'},
]


# Create your views here.
def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    return render(request, 'base/room.html')