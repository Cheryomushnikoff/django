from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def get_post_list(request):
    posts = Post.objects.all()
    my_context = {'posts':posts}

    return render(request, 'blog/post_list.html', context=my_context)


def get_post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)

    context = {
        'post': post
    }

    return render(request, 'blog/post_detail.html', context)

def create_post(request):
    if request.method == 'GET':
        return render(request, 'blog/post_add.html')

    if request.method == 'POST':
        title = request.POST.get('titlePost').strip()
        text = request.POST.get('textPost').strip()

        errors = {}

        if not title:
            errors['title'] = 'Заголовок обязателен'
        if not text:
            errors['text'] = "Текст поста обязательно нужно указывать"

        context = {
            'errors': errors,
            'title': title,
            'text': text,
        }

        print(errors)

        if errors:
            return render(request, 'blog/post_add.html', context=context)

        post = Post.objects.create(title=title, text=text)

        return redirect('post_detail', post_id=post.id )