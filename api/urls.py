from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.GetPosts.as_view(), name='all-posts')
]
