from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	for post in posts:
		if len(post.text) > 50:
			post.text = post.text[:50] + '...'
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, key):
	details = Post.objects.get(pk=key)
	return render(request, 'blog/post_detail.html', {'details': details})