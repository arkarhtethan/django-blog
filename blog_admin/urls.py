from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin_index, name="blog-admin"),
    path('posts/', views.post_admin, name="post-admin"),
    path('login/', views.login_view, name="user-login"),
    path('logout/', views.logout_view, name="user-logout"),
    path('users/delete/<slug:slug>/', views.delete_post, name="delete-post"),

]
