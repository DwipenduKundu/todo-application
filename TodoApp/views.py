from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import todo
import re

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task', '').strip()

        if task:
            existing_task = todo.objects.filter(
                user=request.user,
                todo_name__iexact=task
            ).first()

            if existing_task:
                # If task is completed, reset its status
                if existing_task.status:
                    existing_task.status = False
                    existing_task.save()

                # If already in progress, do nothing

            else:
                # Create a new task
                todo.objects.create(
                    user=request.user,
                    todo_name=task,
                    status=False
                )

        return redirect('home-page')

    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not (len(password) >= 8 and
                re.search(r"[A-Z]", password) and
                re.search(r"[a-z]", password) and
                re.search(r"[0-9]", password) and
                re.search(r"[@$!%*?&]", password)):

            messages.error(request, 'Password must be at least 8 characters and contain '
                           'uppercase, lowercase, number and special character.')
            return redirect('register')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        get_all_user_by_username = User.objects.filter(username=username)
        if get_all_user_by_username:
            messages.error(
                request, 'Error, username already exists, User another.')
            return redirect('register')

        new_user = User.objects.create_user(
            username=username, email=email, password=password)

        new_user.save()

        messages.success(request, 'User successfully created, login now')
        return redirect('login')
    return render(request, 'todoapp/register.html', {})


def LogoutView(request):
    logout(request)
    return redirect('login')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(
                request, 'Error, wrong user details or user does not exist')
            return redirect('login')

    return render(request, 'todoapp/login.html', {})


@login_required(login_url='login')
def DeleteTask(request, id):
    get_todo = get_object_or_404(
        todo, id=id, user=request.user
    )
    get_todo.delete()
    return redirect('home-page')


@login_required(login_url='login')
def Update(request, id):
    get_todo = get_object_or_404(
        todo, id=id, user=request.user
    )

    get_todo.status = not get_todo.status
    get_todo.save()

    return redirect('home-page')