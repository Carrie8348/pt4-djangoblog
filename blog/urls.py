from . import views
from django.urls import path
from .views import profile

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('profile/', profile, name='user_profile'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
] 