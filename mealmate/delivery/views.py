from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    #return HttpResponse("Say Hello my app is working!")
    return render(request, 'index.html')

def open_signup(request):
     return render(request, 'signup.html')

def open_signin(request):
     return render(request, 'signin.html')

def signup(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          email = request.POST.get('email')
          mobile = request.POST.get('mobile')
          address = request.POST.get('address')
          return HttpResponse("Sign up successfull!")
     else:
          return HttpResponse("Invalid Response!")
