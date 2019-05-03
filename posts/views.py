from django.shortcuts import render
from django.views import generic
from .models import Post, Gallery
from category.models import Category
from tags.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):

    return render(request, 'posts/index.html')


class PostIndex(generic.View):

    template_name = 'posts/post_index.html'

    def get(self, request, *args, **kwargs):

        context_data = {
            "object_list": Post.objects.filter(show_in_sample=True).prefetch_related('user', 'category')[:3],
            "latest_posts": Post.objects.all()[:3],
            'gallery_list': Gallery.objects.all()[:4],
            'featured': Post.objects.filter(featured=True)[0]
        }

        return render(request, 'posts/post_index.html', context_data)


class PostList(generic.ListView):

    model = Post

    paginate_by = 4

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().prefetch_related('user', 'category')


class PostDetailView(generic.DetailView):

    model = Post

