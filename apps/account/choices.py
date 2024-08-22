from django.db.models import TextChoices


class AccountRole(TextChoices):
    CUSTOMER = "customer", "Customer"
    PUBLISHER = "publisher", "Publisher"
    WRITER = "writer", "Writer"
    MEMBER = "member", "Member"