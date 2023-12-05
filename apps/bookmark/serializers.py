from rest_framework import serializers

from apps.bookmark.models import Bookmark, Collection
from apps.bookmark.services import BookmarkService


class BookmarkCreateSerializer(serializers.Serializer):
    link = serializers.URLField()

    def create(self, validated_data):
        link = validated_data["link"]
        bookmark_service = BookmarkService(link)
        bookmark = Bookmark.objects.create(
            title=bookmark_service.title,
            description=bookmark_service.description,
            image=bookmark_service.preview_image,
            link=link,
            type_link=bookmark_service.type,
            created_at=bookmark_service.created_at,
            updated_at=bookmark_service.updated_at,
            user=self.context["request"].user,
        )
        bookmark.save()
        return bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "title",
            "description",
            "link_type",
            "image",
            "collection",
        ]


class CollectionSerializer(serializers.ModelSerializer):
    bookmarks = serializers.PrimaryKeyRelatedField(
        queryset=Bookmark.objects.all(), many=True, required=False
    )

    class Meta:
        model = Collection
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "updated_at",
            "bookmarks",
            "user",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "user",
        ]
