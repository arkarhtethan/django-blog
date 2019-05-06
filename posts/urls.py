from django.urls import path, include
from . import views
from .routers import router

app_name = "posts"

urlpatterns = [
    path('',views.PostIndex.as_view(),name='post-index'),
    path('list/',views.PostList.as_view(),name='blog-post-list'),
    path('create/',views.PostCreateView.as_view(),name='post-create'),
    path('update/<slug:slug>/',views.PostUpdateView.as_view(),name='post-update'),
    path('add_comment/<slug:slug>/',views.add_comment,name='add-comment'),
    path('detail/<slug:slug>/',views.PostDetailView.as_view(),name='post-detail'),
    path('search-post/',views.search,name='search'),
    path('admin/',include('blog_admin.urls'),name="admin"),
    path('api/', include(router.urls)),
]