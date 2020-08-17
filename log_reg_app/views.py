from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    new_user = User.objects.register(request.POST)
    request.session['user_id'] = new_user.id
    return redirect('/dashboard')

def login(request):
    result = User.objects.authenticate(request.POST['email'], request.POST['password'])
    if result == False:
        messages.error(request, "Invalid Credentials")
    
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/dashboard')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')