from .models import Post
from category.models import Category
from tags.models import Tag
from users.models import BlogUser

def latest_posts(request):

    latest_posts = Post.objects.all().prefetch_related('category')[:3]

    return {"latest_posts":latest_posts}

def categories(request):

    categories = Category.objects.all()

    return {"categories":categories}

def tags(request):

    tags = Tag.objects.all()

    return {"tags":tags}

def posts_count(request):

    return {"posts_count":Post.objects.count()}

def users_count(request):
    return {"blog_user_count":BlogUser.objects.count()}