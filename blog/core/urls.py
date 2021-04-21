from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_url),

    path('posts/', views.list_posts),
    path('posts/<slug:filename>/', views.view_post),
]
