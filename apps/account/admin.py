from django.contrib import admin

from apps.account.models import Account, Feed, Blog


class BlogInline(admin.StackedInline):
    model = Blog
    extra = 1


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'is_subscribe')
    search_fields = ('id', 'role', 'is_subscribe')
    list_filter = ('id', 'role', 'is_subscribe')
    inlines = (BlogInline,)


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'body', 'website')
    search_fields = ('name', 'website')
    list_filter = ('name', 'website')
    autocomplete_fields = ('account',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')
    search_fields = ('id', 'title')
    list_filter = ('title', 'body')
    autocomplete_fields = ('owner',)


