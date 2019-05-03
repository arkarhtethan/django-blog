from .models import Post
from category.models import Category
from tags.models import Tag

def latest_posts(request):

    latest_posts = Post.objects.all().prefetch_related('user','category')[:3]

    return {"latest_posts":latest_posts}

def categories(request):

    categories = Category.objects.all()

    return {"categories":categories}

def tags(request):

    tags = Tag.objects.all()

    return {"tags":tags}