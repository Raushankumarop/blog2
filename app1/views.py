from django.shortcuts import render
from .models import BlogPost, Category
from .forms import BlogPostForm
import random


# Create your views here.
def index(request):
    posts = BlogPost.objects.filter(status='Published')
    categories = Category.objects.all()
    random_color = f"#{random.randint(0, 0xFFFFFF):06x}"
    context={
        'posts': posts,
        'categories': categories,
        'random_color': random_color
    }
    return render(request, 'index.html', context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BlogPostForm()
    return render(request, 'add.html',  {'form': form})

def all_posts(request):
    posts = BlogPost.objects.all()
    total_posts = posts.count()
    published_count = posts.filter(status='Published').count()
    draft_count = posts.filter(status='Draft').count()
    return render(request, 'all_posts.html', {
        'posts': posts,
        'total_posts': total_posts,
        'published_count': published_count,
        'draft_count': draft_count
    })

