"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

# Import das views da API
from social.api_views import (
    FeedApiView,
    PostListApiView,
    PostDetailApiView,
    PostCreateApiView,
)


def home(request):
    return redirect("feed")


urlpatterns = [
    path("admin/", admin.site.urls),

    # rota raiz
    path("", home, name="home"),

    # apps com prefixos
    path("accounts/", include("accounts.urls")),
    path("posts/", include("posts.urls")),
    path("social/", include("social.urls")),

    # API REST
    path("api/feed/", FeedApiView.as_view(), name="api_feed"),
    path("api/posts/", PostListApiView.as_view(), name="api_posts"),
    path("api/posts/<int:pk>/", PostDetailApiView.as_view(), name="api_post_detail"),
    path("api/posts/create/", PostCreateApiView.as_view(), name="api_post_create"),
]

# 🔥 Servir arquivos de mídia no modo DEBUG
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )