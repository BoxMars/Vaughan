from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from . import models
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
preferred='qwer'

def singup(request):
    is_admin=False
    context = {
        'text' : 'SignUp',
        'height': '600px',
    }
    if len(models.user.objects.all())==0:
        context['text']='SignUp As Admin'
        is_admin=True
    if request.method=='GET':
        return render(request, template_name='background/signup.html',context=context)
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if len(models.user.objects.filter(username=username)) == 0:
            user=models.user(username=username,password=make_password(password,preferred),email=email)
            if is_admin:
                user.group='Admin'
            else:
                user.group='User'
            user.save()
            return redirect(reverse('index'))
        else:
            context['text']='User Exited/Sign Up Again'
            return render(request, template_name='background/signup.html', context=context)

def signin(request):
    context = {
        'text': 'SignIn',
        'height':'450px',
    }
    if request.method=='GET':
        return render(request,template_name='background/signin.html',context=context)
    else:
        username_email=request.POST.get('username')
        if len(models.user.objects.filter(username=username_email))==0 and len(models.user.objects.filter(email=username_email))==0:
            context['text']='User does\'t exited'
            return render(request,template_name='background/signin.html',context=context)
        elif len(models.user.objects.filter(username=username_email))==0 and len(models.user.objects.filter(email=username_email))==1:
            user=models.user.objects.filter(email=username_email)[0]
            password=user.password
            if check_password(request.POST.get('password'),password,preferred):
                return redirect(reverse('index'))
            else:
                context['text']='Wrong Password'
                return render(request, template_name='background/signin.html', context=context)
        elif len(models.user.objects.filter(username=username_email))==1 and len(models.user.objects.filter(email=username_email))==0:
            user=models.user.objects.filter(username=username_email)[0]
            password=user.password
            if check_password(request.POST.get('password'),password,preferred):
                return redirect(reverse('index'))
            else:
                context['text']='Wrong Password'
                return render(request, template_name='background/signin.html', context=context)

