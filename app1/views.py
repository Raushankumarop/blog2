from django.shortcuts import render

# Create your views here.
def index(request):
    posts = [
    {
        "id": 1,
        "title": "Getting Started with Django",
        "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Let's explore how to build your first app.",
        "category": "Development",
        "color_palette": "blue"
    },
    {
        "id": 2,
        "title": "Understanding Tailwind CSS",
        "content": "Tailwind CSS is a utility-first CSS framework packed with classes that can be composed to build any design, directly in your markup.",
        "category": "Web Development",
        "color_palette": "red"
    },
    {
        "id": 3,
        "title": "Mossy Hollow Color Palettes",
        "content": "Exploring nature-inspired color schemes like deep olive, soft sage, and muted earth tones to bring warmth and calmness to user interfaces.",
        "category": "Design",
        "color_palette": "green"
    },
    {
        "id": 4,
        "title": "Git Workflow for Beginners",
        "content": "Version control is essential. Learn how to initialize repositories, stage changes, commit locally, and manage your code with ease.",
        "category": "Development",
        "color_palette": "blue"
    },
    {
        "id": 5,
        "title": "Python Full Stack Development",
        "content": "Combining Python, Django, HTML, CSS, and JavaScript to build robust, scalable, and full-featured web applications from scratch.",
        "category": "Development",
        "color_palette": "blue"
    },
    {
        "id": 6,
        "title": "Building Responsive Layouts",
        "content": "Tips and tricks using CSS Flexbox and Grid combined with utility classes to ensure your website looks great on mobile and desktop.",
        "category": "Web Development",
        "color_palette": "red"
    }
]
    categories = set(post['category'] for post in posts)
    return render(request, 'index.html', {'posts': posts, 'categories': categories})