from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_post, name='add_post'),
    path('all/', views.all_posts, name='all_posts'),
    path('categories/', views.all_categories, name='all_categories'),
    path('post/<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('update/<slug:slug>/', views.update_post, name='update_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'),
]