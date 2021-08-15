from django.shortcuts import render

#Test data
posts=[
    {
        'author': 'Matthew R',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'August 27th, 2021'
    },
    {
        'author': 'Matthew R',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'June 8th, 2021'
    }
]

# Create your views here.
def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')