from contact_form.forms import ContactForm

from django.shortcuts import render
from blog.models import BlogPage


def blog_home(request, template="blog/blog_index_page.html"):
    """
    This is the blog home view.
    """
    # Gather all blogs to display.
    blog_queryset = BlogPage.objects.all()
    print("I'm still here!")
    
    form = ContactForm()
    
    if form._post_clean() is valid:
        # Now do something with the submitted form content.
        print("THE FORM IS VALID...")
    else:
        messages.info("There was a problem in submitting the form.") 
    
    return response(template, request, {'blogpages': blog_queryset})
