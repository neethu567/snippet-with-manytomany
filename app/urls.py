from django.urls import path

from app.views import (
    snippetListCreateAPIView,
    snippetDetailAPIView,
    TagListCreateApiView,
    TagDetailAPIView,
)

urlpatterns = [
    path("snippet-list/", snippetListCreateAPIView.as_view(), name="snippet-list"),
    path(
        "snippet-detail/<int:pk>/", snippetDetailAPIView.as_view(), name="snippet-list"
    ),
    path("tag-list/", TagListCreateApiView.as_view(), name="snippet-list"),
    path("tag-detail/<int:pk>/", TagDetailAPIView.as_view(), name="snippet-list"),
]
