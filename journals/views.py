from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
  title = 'Index page'
  articles = Post.objects.all()
  return render(request, 'index.html', {"title" : title, "articles":articles })
