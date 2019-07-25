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
    return render(request,'index.html',{'page':page,'pageRange':p .page_range,pageno:'page'})
