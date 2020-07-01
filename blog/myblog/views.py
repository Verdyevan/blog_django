from django.shortcuts import render
from .models import Post

#1
def index(request):
    queryset = Post.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)

#1
def blog(request):
    return render(request, 'blog.html')
