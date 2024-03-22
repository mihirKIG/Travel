from imaplib import _Authenticator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        
        if password1 == password2:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
        
            print("USER IS CREATED!")
            return redirect('/')
        else:
            print("USER IS NOT CREATED!")
            return render(request,'register.html')
        
    else:
        print("USER IS NOT CREATED!")
    return render(request,'register.html')

def loginpage(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass1 = request.POST.get('password')
        print(user_name,pass1)
        
        user = authenticate(request,username = user_name , password = pass1)
        
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("User name is incorrect")
    return render(request,'login.html')
