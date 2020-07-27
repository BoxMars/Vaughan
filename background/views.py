from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from . import models
from django.contrib.auth.hashers import make_password
# Create your views here.

def singup(request):
    isAdmin=False
    context = {
        'text' : 'SignUp',

    }
    if len(models.user.objects.all())==0:
        context['text']='SignUp As Admin'
        isAdmin=True
    if request.method=='GET':
        return render(request, template_name='background/signup.html',context=context)
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        print(len(models.user.objects.filter(username=username)))
        if len(models.user.objects.filter(username=username)) == 0:
            user=models.user(username=username,password=make_password(password,'qwer'),email=email)
            if isAdmin:
                user.group='Admin'
            else:
                user.group='User'
            user.save()
            return redirect(reverse('signup'))
        else:
            context['text']='User Exited/Sign Up Again'
            return render(request, template_name='background/signup.html', context=context)