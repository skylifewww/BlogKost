from django.contrib import admin
from article.models import *
from embed_video.admin import AdminVideoMixin
from mptt.admin import MPTTModelAdmin


# Register your models here.

class CommentsInLine(admin.StackedInline):
    model = Comments
    extra = 0


class ArticleAdmin(AdminVideoMixin, admin.ModelAdmin):
    fields = ["article_author", "article_title", "article_video", "article_date", 'short_text_ru',
              'full_text_ru',
              "article_tag", "article_category"]

    inlines = [CommentsInLine]
    list_filter = ["article_date", "article_tag", "article_category", "article_author"]
    search_fields = ["article_title", "article_author", "article_category", "article_tag"]


class  CategoryAdmin(admin.ModelAdmin):
      fields = ['name', 'category_title', 'parent']


# class  AuthorAdmin(admin.ModelAdmin):
#       fields = ['name', 'author_title', 'parent']      
            


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
