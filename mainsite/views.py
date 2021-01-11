from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse


def homepage(request):
    # 获得所有数据项
    posts = Post.objects.all()
    post_lists = list()
    now = datetime.now()

    # locals() 把当前内存中所有的局部变量使用字典类型打包起来
    return render(request, 'index.html', locals())


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post is not None:
            return render(request, 'post.html', locals())

    except:
        return redirect('/')
