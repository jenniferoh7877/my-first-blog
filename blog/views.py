from django.shortcuts import render
from django.utils import timezone
from .models import Post

<<<<<<< HEAD
=======

# Create your views here.

>>>>>>> 0f9ef11d8778667bf491657f34a98d6b3ebff96d
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
