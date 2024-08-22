import os
import random
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from faker import Faker
from apps.article.models import Article, Category, Comment, Advertise
from apps.account.models import Account
from apps.article.choices import Status


def generate_categories(f):
    categories = []
    for _ in range(20):
        cate = Category.objects.create(
            name=f.name(),
        )
        categories.append(cate)


def generate_advertisements(f):
    advertisements = []
    for _ in range(20):
        advertisement = Advertise.objects.create(
            image=f.image_url(),
            url=f.url(),
            expire_date=f.date(pattern='%Y-%m-%d'),
            phone=f.phone_number(),
            is_active=f.boolean()
        )
        advertisements.append(advertisement)


def generate_comments(f):
    comments = []
    owners = list(Account.objects.all())
    articles = list(Article.objects.all())
    for _ in range(20):
        owner = random.choice(owners)
        article = random.choice(articles)
        comment = Comment.objects.create(
            body=f.text(),
            article=article,
            owner=owner
        )
        comments.append(comment)


def generate_articles(f):
    articles = []
    categories = list(Category.objects.all())
    owners = list(Account.objects.all())

    for _ in range(20):
        category = random.choice(categories)
        owner = random.choice(owners)

        article = Article.objects.create(
            title=f.name(),
            slug=f.slug(),  # Ensure a proper slug
            body=f.text(),
            published_at=f.date(pattern='%Y-%m-%d'),  # Correct field name
            status=random.choice([Status.DRAFT, Status.PUBLISHED]),  # Correct usage of choices
            category=category,
            likes=f.random_int(min=50, max=1000),
            image=f.image_url(),
            owner=owner
        )
        articles.append(article)


if __name__ == '__main__':
    f = Faker()
    # generate_categories(f)
    # generate_advertisements(f)
    # generate_articles(f)
    # generate_comments(f)
