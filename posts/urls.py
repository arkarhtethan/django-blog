from django.urls import path, include
from . import views
from .routers import router

app_name = "posts"

urlpatterns = [
    path('',views.PostIndex.as_view(),name='post-index'),
    path('list/',views.PostList.as_view(),name='post-list'),
    path('add_comment/<slug:slug>/',views.add_comment,name='add-comment'),
    path('detail/<slug:slug>/',views.PostDetailView.as_view(),name='post-detail'),
    path('search/',views.search,name='search'),
    path('api/', include(router.urls))
]