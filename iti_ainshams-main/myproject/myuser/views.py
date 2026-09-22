from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import MyUser

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        MyUser.objects.create(
            username=username,
            email=email,
            password=make_password(password)  # بنخزن الباسورد مشفر مش plain text
        )
        return redirect('/login/')
    return render(request, 'myuser/signup.html')


def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = MyUser.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return redirect('/track/')
            else:
                error = 'كلمة السر غلط'
        except MyUser.DoesNotExist:
            error = 'اليوزر ده مش موجود'
    return render(request, 'myuser/login.html', context={'error': error})


def logout(request):
    request.session.flush()
    return redirect('/login/')