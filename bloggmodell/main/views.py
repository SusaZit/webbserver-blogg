
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Author, Post

# Create your views here.
def main(request):
    posts=Post.objects.all()
    
    return render(request,"index.html",{"posts":posts})
    

        

