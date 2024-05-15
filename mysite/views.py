from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from mysite.models import Post


# Create your views here.
def homepage(request):
    # 2-2
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<hr>")
        post_lists.append("<small>" + str(post.body) + "</small><br><br>")
    return HttpResponse(post_lists)

    # 2-3

def index(request):
    posts = Post.objects.all()
    post_lists = list()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

