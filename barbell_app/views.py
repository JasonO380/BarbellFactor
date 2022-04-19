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
    #print(user_list)
    #users = User.objects.get('user_name'),#New code trying to print out all clients info
    users = User()
    username = request.POST.get('user_name','')
    # client = vars(users)
    # for key in client:
    #     print(key)
    #     print(client[key])
    print('check user name')
    print(users)
    print(username)
    #print(User.objects.all())
    # client = vars(users)
    # for item in client:
    #     print(item)
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
        print('This works hopefully')
        print(new_user)
        new_user.save()
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

#####New one tring to get all users populated on html page#####
def athletes(request):
    athlete = User.objects.all
    context = {
        'athlete': athlete,

    }
    return render(request, 'athletes.html',context)

def member(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user,
    }
    return render(request, 'member.html', context)

def weightlifting(request):
    return render(request, 'member.html')

def squat(request):
    return render(request, 'squat.html')

def workout(request):
    return render(request, 'workout.html')

def logout(request):
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    request.session.flush()
    print(request.session)
    return redirect('/')
