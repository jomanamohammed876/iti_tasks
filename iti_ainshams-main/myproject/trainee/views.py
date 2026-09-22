from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Trainee

def alltrainee(request):
    context={'trainee':Trainee.objects.all()}
    return render(request, 'trainee/trainee.html', context=context)

def gettrainee(request):
    return HttpResponse("<h1>inside first trainee</h1>")

def inserttrainee(request):
    if request.method =='POST':
        name=request.POST['trname']
        email=request.POST['tremail']
        image=request.FILES.get('trimage')
        Trainee.objects.create(name=name,email=email,image=image)
        return HttpResponse("<h1>inserted successfully</h1>")

    return render(request, 'trainee/insert.html')
def updatetrainee(request,id):
    trainee = Trainee.objects.get(id=id)
    if request.method == 'POST':
        trainee.name = request.POST['trname']
        trainee.email = request.POST['tremail']
        image = request.FILES.get('trimage')
        if image:
            trainee.image = image
        trainee.save()
        return redirect('/trainee/')
    return render(request, 'trainee/updatetrainee.html', context={'trainee': trainee})

def deletetrainee(request,id):
    Trainee.objects.filter(id=id).update(status=False)
    return redirect('/trainee/')
