from django.shortcuts import render
from .models import Post
def get_post_list(request):
    posts = Post.objects.all()
    my_context = {'posts':posts}

    return render(request, 'post_list.html', context=my_context)
