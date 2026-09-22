from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Track
# Create your views here.
def alltracks(request):
    #{"id":1,"name":"python"}
    tracks=Track.objects.all().order_by('id')
    return render(request, 'tracks/list.html', context={'tracks':tracks})

def gettrack(request):
    return HttpResponse("<h1>inside first track</h1>")

def inserttrack(request):
    if request.method =='POST':
        name=request.POST['trname']
        Track.objects.create(name=name)
        return redirect('/track/')
    return render(request , 'tracks/inserttrack.html')

def updatetrack(request,id):
    if request.method =='POST':
        name = request.POST['trname']
        Track.objects.filter(id=id).update(name=name)
        return redirect('/track/')
        # return redirect('https://www.youtube.com/')

    return render(request, 'tracks/updatetrack.html',
                  context={'track':Track.objects.get(id=id)})

def deletetrack(request,id):
    Track.objects.filter(id=id).delete()
    return redirect('/track/')