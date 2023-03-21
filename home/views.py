from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from .models import *

# Create your views here.


def home(request):
    blog=BlogModel.objects.all()
    context={'blog':blog}
    return render(request,'home.html',context)

def add_blog(request):
    from .form import blogForm
    context = {'form': blogForm}
 
    if request.method == 'POST':
            form = blogForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(blog_obj)
            return redirect('/')

    return render(request, 'add_bloge.html', context)

def blog_page(request,slug):
    data=BlogModel.objects.filter(slug=slug)
    recommanded=BlogModel.objects.all()[:5]
    context={'data':data,'r':recommanded}
    return render(request,'page.html',context)


def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if User is not None:
            return redirect('/')
        else:
            return HttpResponse('username and password incorrect')
    return render(request,'login.html')  




def all_blogs(request):
    data =BlogModel.objects.all()
    return render(request,'all_blogs.html',{'data':data})


def delete_blog(request,pk):
    
    item=BlogModel.objects.get(pk=pk).delete()
    return redirect(all_blogs)

def logout_user(request):
    logout(request)
    return redirect('/')