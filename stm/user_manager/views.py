from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.models import auth, User
from django.http.response import HttpResponse
# Create your views here.

def login_register_page(request):
    return render(request, 'login_register.html')

def login(request):
    
    assert request.method == 'POST'

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    
    # user = auth.authenticate(username=username, password=password)
    # 
    # if user is not None:
    #     auth.login(request, user)
    #     return redirect('register')
    # else:
    #     messages.info(request, 'Invalid Credentials')
    #     return redirect('login')

    print(username)
    print(password)
    return redirect('login_register_page')
     

def register(request):
    
    assert request.method == 'POST'

    name = request.POST.get('name', False)
    username = request.POST.get('username', False)
    email = request.POST.get('email', False)
    password = request.POST.get('password', False)
    re_password = request.POST.get('repeat_password', False)

    # if password != re_password:
    #     messages.info(request, "Password not matching.")
    #     return register('register')

    # elif User.objects.filter(username=username).exists():
    #     messages.info(request, "Username Already Taken")
    #     return register('register')
    #     
    # elif User.objects/filter(email=email).exists():
    #     messages.info(request, "Email ID Already Taken")
    #     return register('register')

    # else:
    #     user = User.objects.create_user(name=name,
    #                                     username=username,
    #                                     email=email,
    #                                     password=password)
    #     user.save()
    #     messages.info(request, "User Created!")
    #     return redirect('login')

    print(name)
    print(username)
    print(email)
    print(password)
    print(re_password)
    return redirect('login_register_page')