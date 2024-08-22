from apps.article.models import Category, Tag, Article


def category_list(request):
    articless = Article.objects.order_by('likes')
    category = Category.objects.all()
    tags = Tag.objects.all()
    return {"categories": category, "tags": tags, "articles": articless}
