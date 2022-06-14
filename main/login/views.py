import sys
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .form import userForm, blogForm
from .function import handle_uploaded_file
from django.utils import timezone
from .models import user, blog
from django.contrib.auth.decorators import login_required
from .task import test_func

# Create your views here.


def view(request):
    u = user.objects.all()
    return render(request, 'show.html',{'u': u})


def login(request):
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']

        val = user.objects.filter(username=u, password=p).count()

        if val == 1:
            data = user.objects.filter(username=u, password=p)
            print('=====', data)
            for items in data:
                request.session['id'] = items.id
                request.session['username'] = items.username
                return redirect('/blog/')
        else:
            messages.error(request, 'invalid username or password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


@login_required
def logout(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/login/')
            except:
                print('---', sys.exc_info())
        else:
            pass
    else:
        form = userForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def insert(request):
    b = blog.objects.all()
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES)
        print('++++', form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['img'])
                form.save()
                return redirect('/blog/')
            except:
                print('+++++++++++++++++', sys.exc_info())
        else:
            pass
    else:
        form = blogForm()
        return render(request, 'insert.html', {'form': form, 'b': b})

    return render(request, 'insert.html', {'form': form})


def blog_show(request):
    b = blog.objects.all()
    return render(request, 'blog.html', {'b': b})


def blog_details(request, id=0):
    b = blog.objects.filter(id=id)
    return render(request, "blog_details.html", {'b': b})


def edit(request, id):
    b = blog.objects.get(id=id)
    return render(request, "edit.html", {"b": b})


def update(request, id):
    b = blog.objects.get(id=id)

    print("+++++++++++", b)
    if request.method == "POST":
        form = blogForm(request.POST,instance=b)
        print("--------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/blog/")
            except:
                print("--------", sys.exc_info())

        return render(request, 'edit.html', {'b': b})


def delete(request, id):
    b = blog.objects.filter(id=id)
    b.delete()
    return redirect("/blog/")


def admin(request):
    b = blog.objects.all()
    return render(request, 'admin.html', {'b':b})


def home(request):
    return render(request, 'home.html')


def test(request):
    test_func.delay()
    return render(request, 'home.html')
