from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post

@api_view(["GET"])
def posts_api(request):
    data = [
        {
            "author": p.author.username,
            "content": p.content,
            "created_at": p.created_at
        }
        for p in Post.objects.all()
    ]
    return Response(data)