from django.urls import path

from apps.bookmark.views import (
    BookmarkDetailAPIView,
    BookmarkListCrateAPIView,
    CollectionDetailAPIView,
    CollectionListCreateAPIView,
)

urlpatterns = [
    path("bookmarks", BookmarkListCrateAPIView.as_view(), name="bookmark_list"),
    path("bookmark/<int:pk>", BookmarkDetailAPIView.as_view(), name="bookmark_detail"),
    path("collections", CollectionListCreateAPIView.as_view(), name="collection_list"),
    path(
        "collection/<int:pk>",
        CollectionDetailAPIView.as_view(),
        name="collection_detail",
    ),
]
