from datetime import timedelta

from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import CharField, SlugField, TextField, DateTimeField, TextChoices, Manager, ForeignKey, CASCADE, \
    IntegerField, ImageField, SET_NULL, URLField, BooleanField, ManyToManyField
from django.utils import timezone
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

from apps.article.choices import Status
from apps.article.managers import PublishManager, ActiveAdvertiseManager
from apps.shared.models import BaseModel
from django.utils.translation import gettext_lazy as _

from config import settings


class Article(BaseModel):
    # managers
    objects = Manager()
    published = PublishManager()

    # fields
    title = CharField(verbose_name=_("Title"), max_length=256)
    slug = SlugField(verbose_name=_("SLG"), unique=True, blank=True, max_length=256)
    body = RichTextUploadingField(verbose_name=_("Body"))
    published_at = DateTimeField(verbose_name=_("published"), default=timezone.now)
    status = CharField(verbose_name=_("Status"), max_length=15, choices=Status.choices, default=Status.DRAFT)
    category = ForeignKey(verbose_name=_("Category"), to="article.Category", on_delete=CASCADE,
                          related_name='artcicles')
    likes = IntegerField(verbose_name=_("Likes"), default=0)
    owner = ForeignKey(verbose_name=_("Owner"), to="account.Account", on_delete=SET_NULL, related_name='article',
                       null=True)
    is_active = BooleanField(verbose_name=_("Is Active"), default=False)
    tags = ManyToManyField(verbose_name=_("Tags"), to="article.Tag", related_name="articles")

    def translate_to_eng(self, s: str) -> str:
        d = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
            'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y',
            'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
            'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
            'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y',
            'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
        }

        return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        for lang_code, _ in settings.LANGUAGES:

            title_translated = getattr(self, f'title_{lang_code}', None)

            if title_translated:
                if lang_code == "ru":
                    slug_translated = slugify(
                        f"{self.published_at.strftime('%Y-%m-%d')} {self.translate_to_eng(title_translated)}")
                else:
                    slug_translated = slugify(f"{self.published_at.strftime('%Y-%m-%d')} {title_translated}")
                setattr(self, f'slug_{lang_code}', slug_translated)

        super().save(force_insert, force_update, using, update_fields)


    def __str__(self):
        return self.title


class Category(BaseModel):
    name = CharField(max_length=64)

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name


class Comment(BaseModel):
    body = TextField()
    owner = ForeignKey("account.Account", CASCADE, "comments")
    article = ForeignKey("article.Article", CASCADE, "comments")


def advertise_expire(*args, **kwargs):
    return timezone.now()+timedelta(days=3)


class Advertise(BaseModel):
    objects = Manager()
    active = ActiveAdvertiseManager()

    image = ImageField(upload_to="advertise/images/")
    url = URLField()
    expire_date = DateTimeField(default=advertise_expire)
    phone = PhoneNumberField(region="UZ")
    is_active = BooleanField()

    def __str__(self):
        return self.url


class Tag(BaseModel):
    name = CharField(max_length=56)

    def __str__(self):
        return self.name
