from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request,pageno=1):
    postList = Post.objects.all().order_by('-created')
    # for i in postList:
    #     print(i.title)
    p=Paginator(postList,2)
    page = p.page(pageno)
    return render(request,'index.html',{'page':page,'pageRange':p.page_range})
def detail(request,id):
    post = Post.objects.get(pk=id)
    return render(request,'detail.html',{'post':post})
def aboutme(request):
    return render(request,'aboutme.html')
def category(request,cateid):
    print(cateid)
    postList = Post.objects.filter(category_id=cateid).order_by('-created')
    return render(request,'categoryl.html',{'postList':postList})
def archive(request,year=None,month=None):
    print(year,month)
    if year and month:

        postList = Post.objects.filter(created__year=year,created__month=month).order_by('-created')
    else:
        postList = Post.objects.all().order_by('-created')
    return render(request,'categoryl.html',{'postList':postList})