# isort:skip_file
from django.urls import path

from apps.bookmark.views import (
    BookmarkDetailAPIView,
    BookmarkListCrateAPIView,
    CollectionDetailAPIView,
    CollectionListCreateAPIView,
)

urlpatterns = [
    path("bookmarks", BookmarkListCrateAPIView.as_view(), name="bookmark-list-create"),
    path("bookmark/<int:pk>", BookmarkDetailAPIView.as_view(), name="bookmark-detail"),
    path(
        "collections",
        CollectionListCreateAPIView.as_view(),
        name="collection-list-create",
    ),
    path(
        "collection/<int:pk>",
        CollectionDetailAPIView.as_view(),
        name="collection-detail",
    ),
]
