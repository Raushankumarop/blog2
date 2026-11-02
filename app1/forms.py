from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'category', 'author_name', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 bg-white rounded-md my-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-700',
                'placeholder': 'Getting Started with Django'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md my-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-700 bg-gray-50',
                'placeholder': 'getting-started-with-django'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md my-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-700 bg-white'
            }),
            'author_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border bg-white border-gray-300 rounded-md my-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-700',
                'placeholder': 'Arjun Kumar'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border bg-white border-gray-300 rounded-md mt-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-700',
                'rows': 5,
                'placeholder': 'Write your post content here...'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md mt-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-700 bg-white'
            }),
        }