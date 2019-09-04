from django.shortcuts import render
from blog.models import BlogPage


def blog_home(request, template="blog/blog_index_page.html"):
    """
    This is the blog home view.
    """
    # Gather all blogs to display.
    blog_queryset = BlogPage.objects.all()
    print("I'm still here!")
    
    return response(template, request, {'blogpages': blog_queryset})
