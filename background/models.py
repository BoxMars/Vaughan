from django.db import models
import uuid,markdown,re
from django.utils import timezone

# Create your models here.

class user(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=255)
    group=models.CharField(max_length=200,default='User')
    created = models.DateTimeField(default=timezone.now)


class article(models.Model):
    author=models.ForeignKey('user',on_delete=models.PROTECT)
    title=models.CharField(max_length=200)
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)
    tag=models.CharField(max_length=200,default='untaged')
    body=models.TextField()

    def get_details(self):
        body=self.body
        body=markdown.markdown(body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
         'markdown.extensions.toc',
        ])
        limit=150
        context={
            'id':self.id,
            'title':self.title,
            'created':self.created,
            'updated':self.updated,
            'tag':self.tag,
            'body':self.body,
            'full_body':self.body,
            'markdown':body,
            'full_markdown':body,
            'author':self.author.username,
        }
        if len(self.body)>limit:
            context['body']=context['body'][:limit]

        context['markdown']=re.sub('\<[^>]*\>','',context['markdown'])
        if len(context['markdown']) > limit:
            context['markdown'] = context['markdown'][:limit]
        # print(context['markdown'])
        return context
