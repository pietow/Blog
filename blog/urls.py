from . import views
from django.urls import path

urlpatterns = [
    path('photo/', views.GalleryList.as_view(), name='gallery'),
    path('reisen/', views.PostList.as_view(), name='gallery'),
    path('<slug:slug>/', views.HomeDetail.as_view(), name='home_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
