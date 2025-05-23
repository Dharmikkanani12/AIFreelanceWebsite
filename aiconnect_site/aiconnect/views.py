from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProjectForm
from .models import Project, User

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    developers = User.objects.filter(user_type='freelancer')
    return render(request, 'aiconnect/home.html', {'projects': projects, 'developers': developers})

def projects_view(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'aiconnect/projects.html', {'projects': projects})

def developers_view(request):
    developers = User.objects.filter(user_type='freelancer')
    return render(request, 'aiconnect/developers.html', {'developers': developers})

@login_required
def postproject_view(request):
    if request.user.user_type != 'company':
        return redirect('home')
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.company = request.user
            project.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'aiconnect/postproject.html', {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'aiconnect/signup.html', {'form': form})

def login_view(request):
    error = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid credentials'
    return render(request, 'aiconnect/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')