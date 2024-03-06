from django.urls import path, include
from rest_framework import routers
from .views import *
from api2 import views

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('post', PostViewSet)
router.register('comment', CommentViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
    
# ]

urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name="post-detail"),
    path('comment/', views.CommentCreateAPIView.as_view(), name="comment-list"),
    path('post/<int:pk>/like/', views.PostLikeAPIView2.as_view(), name="post-like"),
    path('catetag/', views.CateTagAPIView.as_view(), name='catetag'),
]