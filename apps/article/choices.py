from django.db.models import TextChoices


class Status(TextChoices):
    DRAFT = ("df", "Draft"),
    PUBLISHED = ("pb", "Published")