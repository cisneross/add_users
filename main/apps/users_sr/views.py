from django.shortcuts import render, redirect
from .models import *
# Create your views here.
#main table page
def table(request):
    usrs = User.objects.all()
    context={
        'users': usrs,
    }
    return render(request,'users_sr/index.html',context)
#renders the registration page
def add(request):
    return render(request,'users_sr/add_user.html')
#creates the user in db
def process(request):
    user=User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
    print(user)
    return redirect('/users/new')
# deletes a user
def destroy(request,id):
    User.objects.get(id=id).delete()
    return redirect('/users')
# edits a preexisting record
def edit(request,id):
    print('I made it')
    context ={
        'user': User.objects.get(id=id)
    }
    request.session['id']=id
    print(request.session['id'])
    return render(request,'users_sr/edit_user.html',context)
def process_edit(request):
    print('I made it here tooooo')
    user=User.objects.get(id=request.session['id'])
    user.first_name=request.POST['first_name']
    user.last_name=request.POST['last_name']
    user.email=request.POST['email']
    user.save()
    return redirect('/users')
def show(request,id):
    print('I made it to this stop')
    context ={
        'user': User.objects.get(id=id)
    }
    return render(request,'users_sr/display.html',context)
