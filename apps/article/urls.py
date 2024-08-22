from django.urls import path

from apps.article.views import HomeView, CategoryView, ArticleView, TagView

app_name = 'article'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('category/<pk>/', CategoryView.as_view(), name="category"),
    path('article/<pk>/', ArticleView.as_view(), name="article-detail"),
    path('tags/<pk>/', TagView.as_view(), name="tag"),
]
