from . import views
from django.urls import path
from .views import profile

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('profile/', profile, name='user_profile'),
    path('edit_profile/', views.profile_update, name='edit_profile'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
] 