from rest_framework import generics, permissions
from posts.models import Post  # ✅ corrigido: Post vem do app "posts"
from .models import Follow
from .serializers import PostSerializer


# Feed: posts apenas de quem o usuário segue
class FeedApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following = Follow.objects.filter(
            follower=self.request.user
        ).values_list("following_id", flat=True)
        return Post.objects.filter(
            author_id__in=following
        ).order_by("-created_at")


# Listar todos os posts (público)
class PostListApiView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


# Detalhar um post específico
class PostDetailApiView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


# Criar novo post (apenas autenticado)
class PostCreateApiView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)