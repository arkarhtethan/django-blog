from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from users.models import BlogUser
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/posts/admin/login/")
def admin_index(request):
    
    context = {
        'object_list':BlogUser.objects.all()
    }

    return render(request,'blog_admin/admin_index.html',context)

@login_required(login_url="/posts/admin/login/")
def post_admin(request):
    
    context = {
        'object_list':Post.objects.all()
    }
    return render(request,'blog_admin/post_admin.html', context)

@login_required(login_url="/posts/admin/login/")
def delete_post(request, slug):

    post = get_object_or_404(Post,slug=slug)

    post.delete()

    return redirect(reverse("posts:post-admin"))

def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username',None)

        password = request.POST.get('password', None)

        if username and password:

            user = authenticate(username=username, password=password)

            if user:
                
                login(request, user)

                return redirect(reverse("posts:blog-admin"))

    return render(request,'blog_admin/authentication/login.html')

def logout_view(request):

    logout(request)

    return redirect(reverse('posts:user-login'))
