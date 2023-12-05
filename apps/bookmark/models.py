from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Collection(models.Model):
    """Модель коллекции"""

    title = models.CharField(max_length=100, unique=True, verbose_name="Название")
    description = models.TextField(max_length=1000, blank=True, verbose_name="Описание")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="collections",
        verbose_name="Владелец",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = verbose_name
        ordering = ["title"]

    def __str__(self):
        return self.title


class LinkTypes(models.TextChoices):
    """Типы закладок."""

    WEBSITE = "website", "website"
    BOOK = "book", "book"
    ARTICLE = "article", "article"
    MUSIC = "music", "music"
    VIDEO = "video", "video"


class Bookmark(models.Model):
    """Модель закладки"""

    title = models.CharField(max_length=256, blank=True, verbose_name="Название")
    description = models.TextField(max_length=500, blank=True, verbose_name="Описание")
    link = models.URLField(verbose_name="Ссылка")
    type_link = models.CharField(
        choices=LinkTypes.choices, default=LinkTypes.WEBSITE, verbose_name="Тип ссылки"
    )
    image = models.URLField(verbose_name="Изображение")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата и время изменения"
    )
    collection = models.ForeignKey(
        "Collection",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="bookmarks",
        verbose_name="коллекция",
    )
    user = models.ForeignKey(
        User,
        related_name="bookmarks",
        on_delete=models.CASCADE,
        verbose_name="владелец",
    )

    class Meta:
        verbose_name = "Закладка"
        verbose_name_plural = verbose_name
        ordering = ["title"]

    def __str__(self):
        if self.title:
            return self.title
        return self.link
