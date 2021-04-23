from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import User, Video
import bcrypt

# Create your views here.

def index(request):
    video=Video.objects.all()
    return render(request, 'index.html',{'video':video})

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def make_account(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.user_validator(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/register')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return render(request, 'member.html')
    

def client(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/login')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/member')

def member(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user,
    }
    return render(request, 'member.html', context)

def logout(request):
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    request.session.flush()
    print(request.session)
    return redirect('/')
