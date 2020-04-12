from django.urls import path
from . import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.PostList.as_view(),name='blog-index'),
    path('post/<int:pk>', blog_views.DetailPost.as_view(),name='blog-detail'),
    path('post/<int:pk>/update', blog_views.UpdatePoste.as_view(),name='blog-update'),
    path('post/<int:pk>/delete', blog_views.DeletePost.as_view(template_name='blog/post_delete.html'),name='blog-delete'),
    path('create/',blog_views.CreatePost.as_view(), name='blog-create'),
]