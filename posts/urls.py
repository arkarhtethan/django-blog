from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('',views.PostIndex.as_view(),name='post-index'),
    path('list/',views.PostList.as_view(),name='post-list'),
    path('detail/<slug:slug>/',views.PostDetailView.as_view(),name='post-detail')
]