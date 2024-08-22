from modeltranslation.translator import TranslationOptions, translator

from apps.article.models import Article


class ArticleTranslationOption(TranslationOptions):
    fields = ('title', 'body', 'slug')


translator.register(Article, ArticleTranslationOption)
