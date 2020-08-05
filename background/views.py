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
            response = redirect(reverse('index'))
            response.set_cookie(key='se', value=make_password(user.uuid), max_age=None)
            return response
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
                response=redirect(reverse('index'))
                response.set_cookie(key='user', value=user.uuid, max_age=None)
                response.set_cookie(key='se', value=make_password(user.uuid, user.username), max_age=None)
                return response
            else:
                context['text']='Wrong Password'
                return render(request, template_name='background/signin.html', context=context)
        elif len(models.user.objects.filter(username=username_email))==1 and len(models.user.objects.filter(email=username_email))==0:
            user=models.user.objects.filter(username=username_email)[0]
            password=user.password
            if check_password(request.POST.get('password'),password,preferred):
                response = redirect(reverse('index'))
                response.set_cookie(key='user', value=user.uuid,max_age=None)
                response.set_cookie(key='se', value=make_password(user.uuid, user.username),max_age=None)
                return response
            else:
                context['text']='Wrong Password'
                return render(request, template_name='background/signin.html', context=context)

def test(request):
    user=models.user.objects.filter(username='Box').first()
    test_article=models.article()
    test_article.title='test'
    test_article.body="# Right now, polls say Joe Biden has a healthy lead over President Trump. But we’ve been here before (cue 2016), and the polls were, frankly, wrong. One man, however, was not. The historian Allan Lichtman was the lonely forecaster who predicted Mr. Trump’s victory in 2016 — and also prophesied the president would be impeached. That’s two for two. But Professor Lichtman’s record goes much deeper. In 1980, he developed a presidential prediction model that retrospectively accounted for 120 years of U.S. election history. Over the past four decades, his system has accurately called presidential victors, from Ronald Reagan in ’84 to, well, Mr. Trump in 2016.In the video Op-Ed above, Professor Lichtman walks us through his system, which identifies 13 “keys” to winning the White House. Each key is a binary statement: true or false. And if six or more keys are false, the party in the White House is on its way out.So what do the keys predict for 2020? To learn that, you’ll have to watch the video."
    test_article.author=user
    test_article.save()
    return render(request, template_name='background/signup.html')