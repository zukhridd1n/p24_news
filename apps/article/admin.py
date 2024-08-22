from django.contrib import admin
from django.contrib.admin import StackedInline, TabularInline
from modeltranslation.admin import TranslationAdmin

from apps.article.models import Article, Category, Comment, Advertise, Tag


class ArticleInline(StackedInline):
    model = Article
    extra = 2


class CommentInline(TabularInline):
    model = Comment
    extra = 1


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    # list_display = ('title', 'body', 'slug', 'is_active', 'owner', 'likes')
    # list_filter = ('category', 'is_active', 'owner')
    # date_hierarchy = 'published_at'
    # prepopulated_fields = {'slug': ('title', 'published_at')}
    # search_fields = ('title', 'body')
    # inlines = (CommentInline,)
    # autocomplete_fields = ('category', 'tags')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (ArticleInline,)
    search_fields = ('name', 'tag')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('updated_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'owner', 'article')
    list_filter = ('owner', 'article')
    date_hierarchy = 'created_at'


@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_filter = ('is_active',)
    date_hierarchy = 'expire_date'
    list_display = ('url', 'expire_date', 'phone')
    list_display_links = ('expire_date',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
