from django.shortcuts import render
from blog.models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .permissions import IsSuperUserOrStaffOrReadOnly, IsAuthorOrReadOnly, IsStaffOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    filterset_fields = ['status', 'author__username']
    search_fields = ['title', 'content', 'author__first_name', 'author__last_name']
    ordering_fields = ['publish', 'status']

    def get_permissions(self):
        if self.action == ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsSuperUserOrStaffOrReadOnly']
