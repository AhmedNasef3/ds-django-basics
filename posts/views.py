from django.shortcuts import render
from .models import post
# Create your views here.
def post_list(request):
    data=post.objects.all()
    return render(request,'posts.html',{'posts':data})


def post_detail(request):
    pass
