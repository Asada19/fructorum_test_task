import os

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.bookmark.models import Bookmark, Collection, LinkTypes

User = get_user_model()


class BookmarkAPITests(APITestCase):
    def setUp(self):
        username = os.environ.get("TEST_USERNAME", "testuser")
        password = os.environ.get("TEST_PASSWORD", "testpassword")

        self.user = get_user_model().objects.create_user(
            username=username, password=password
        )

        self.bookmark = Bookmark.objects.create(
            title="Test Bookma  rk",
            description="Test Description",
            link="http://example.com",
            type_link=LinkTypes.WEBSITE,
            image="http://example.com/image.jpg",
            user=self.user,
        )

        self.collection = Collection.objects.create(
            title="Test Collection",
            description="Test Collection Description",
            user=self.user,
        )

    def test_create_bookmark(self):
        url = reverse("bookmark-list-create")
        data = {"link": "http://example.com/bookmark"}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bookmark.objects.count(), 2)

    def test_retrieve_bookmark(self):
        url = reverse("bookmark-detail", args=[self.bookmark.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Bookmark")


class CollectionAPITests(APITestCase):
    def setUp(self):
        username = os.environ.get("TEST_USERNAME", "testuser")
        password = os.environ.get("TEST_PASSWORD", "testpassword")

        self.user = get_user_model().objects.create_user(
            username=username, password=password
        )

        self.collection = Collection.objects.create(
            title="Test Collection",
            description="Test Collection Description",
            user=self.user,
        )

    def test_create_collection(self):
        url = reverse("collection-list-create")
        data = {"title": "New Collection", "description": "New Collection Description"}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Collection.objects.count(), 2)

    def test_retrieve_collection(self):
        url = reverse("collection-detail", args=[self.collection.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Collection")
