from django.http import request
from django.shortcuts import redirect, render
from .models import BlogPost, Category
from .forms import BlogPostForm
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
@login_required
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
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

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def blog_post_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    categories = Category.objects.all()
    posts = BlogPost.objects.filter(status='Published').order_by('-created_at')[:5]
    return render(request, 'blog_detail.html', {'blog': post, 'categories': categories, 'posts': posts})

def category_posts(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = BlogPost.objects.filter(category=category)
    return render(request, 'category_wise.html', {'category': category, 'posts': posts})
@login_required
def update_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('all_posts')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'update.html', {'form': form, 'post': post})
@login_required
def delete_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('all_posts')
    return render(request, 'delete.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user against the database
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'authentication/login.html')