from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import Post, Gallery, Comment
from category.models import Category
from tags.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

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


def add_comment(request, slug):
    """

       slug: post slug

    """

    print(request.POST)

    if request.method == "POST":

        username = request.POST.get('username')

        useremail = request.POST.get('useremail')

        usercomment = request.POST.get('usercomment')

        post = Post.objects.get(slug=slug)

        Comment.objects.create(
            name=username, email=useremail, text=usercomment, post=post)

    return redirect(reverse("posts:post-detail", kwargs={"slug": slug}))


def search(request):

    q = request.GET.get('q', None)

    if len(q) > 0:

        q = q.strip()

        object_list = Post.objects.prefetch_related('user', 'category').filter(
            Q(title__icontains=q) |
            Q(category__name__icontains=q) |
            Q(content__icontains=q) |
            Q(user__name__icontains=q)
        )

        context = {
            "object_list": object_list
        }

        return render(request, 'posts/post_list.html', context)

    return redirect(reverse("posts:post-list"))
