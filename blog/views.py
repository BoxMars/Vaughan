from django.shortcuts import render
from background import models as background_models
import markdown
# Create your views here.

def index(request):
    context= {
        'articles':[]
    }
    articles=background_models.article.objects.all()
    for i in articles:
        context['articles'].append(i.get_details())
    return render(request,template_name='blog/index.html',context=context)