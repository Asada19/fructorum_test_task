from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.bookmark.models import Bookmark, Collection
from apps.bookmark.permissions import IsOwner
from apps.bookmark.serializers import (
    BookmarkCreateSerializer,
    BookmarkSerializer,
    CollectionSerializer,
)


class BookmarkListCrateAPIView(ListCreateAPIView):
    model = Bookmark
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkCreateSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BookmarkSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, args=self.request.data)


class BookmarkDetailAPIView(RetrieveUpdateDestroyAPIView):
    model = Bookmark
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class CollectionListCreateAPIView(ListCreateAPIView):
    model = Collection
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, args=self.request.data)


class CollectionDetailAPIView(RetrieveUpdateDestroyAPIView):
    model = Collection
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated,)
