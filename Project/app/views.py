from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def home(request):
    userofList = UserOfPlayList.objects.get(user=request.user)
    playlist = MyPlaylist.objects.filter(user = userofList)
    return render(request,'home.html',{'playlist':playlist})

@login_required(login_url='/')
def intoPlayList(request,id):
    playlist = MyPlaylist.objects.get(pk=id)
    videos = Video.objects.filter(belongTo = playlist)
    return render(request,'playList.html',{'videos':videos,'id':id})

@login_required(login_url='/')
def viewFavs(request):
    userofList = UserOfPlayList.objects.get(user=request.user)
    playlist = MyPlaylist.objects.filter(user = userofList,favourite=True)
    return render(request,'fav.html',{'playlist':playlist})

@login_required(login_url='/')
def addPlaylist(request):
    if request.method == "POST":
        name = request.POST.get('namelist')
        desc = request.POST.get('description')
        user = UserOfPlayList.objects.get(user=request.user)
        newplalist = MyPlaylist(user=user,description=desc,name=name) 
        newplalist.save()
        return redirect('/home/')
    return render(request,'home.html',{})

@login_required(login_url='/')
def deletePlayList(request,id):
    playlist = MyPlaylist.objects.get(pk=id)
    playlist.delete()
    return redirect('/home/')

@login_required(login_url='/')
def addItem(request,id):
    print(id)
    return render(request,'addingForm.html',{'idp':id})

@login_required(login_url='/')
def add(request,id):
    if request.method == "POST":
        link = request.POST.get("link")
        name = request.POST.get("Name")
        desc = request.POST.get("description")
        playlist = MyPlaylist.objects.get(pk=id)
        video = Video(belongTo=playlist,name=name,description=desc,link=link)
        video.save()
        return redirect(f'/playlist/{id}/')
    return redirect(f'/playlist/{id}/')

@login_required(login_url='/')
def deleteVideo(request,id,idp):
    video = Video.objects.get(pk = id)
    video.delete()
    return redirect(f'/playlist/{idp}/')

def register(request):
    if request.method == "POST":
        user = User()
        username = request.POST.get('name')
        user.first_name = request.POST.get('username')
        user.username = username
        password = request.POST.get('password')
        user.set_password(password)
        user.save()

        newUser = UserOfPlayList(user=user,username=username)
        newUser.save()

        return redirect('/')
    return render(request,'registerForm.html',{})

def loginForm(request):
    if request.method=="POST":
        name = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request,username=name,password=passw)

        if user is not None:
            login(request,user)
            return redirect('/home/')
        else:
            messages.info(request,'UserName or Password is Incorrect')

    return render(request,'loginForm.html',{})


@login_required(login_url='/')
def loggingOut(request):
    logout(request)
    return render(request,'loginForm.html',{})