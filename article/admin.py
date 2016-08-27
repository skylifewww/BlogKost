from django.contrib import admin
from article.models import *
from embed_video.admin import AdminVideoMixin
from mptt.admin import MPTTModelAdmin


# Register your models here.

# class CommentsInLine(admin.StackedInline):
#     model = Comments
#     extra = 0


class ArticleAdmin(AdminVideoMixin, admin.ModelAdmin):
    fields = ["article_author", "article_title", "article_video", 'video_published', "article_date", 'short_text_ru',
              'full_text_ru', 'text_published', 'slug',
              "article_tag", "article_category", "video_only", "written_only"]

    # inlines = [CommentsInLine]
    list_filter = ["article_date", "article_tag", "article_category", "article_author", 'video_published', 'text_published', "video_only", "written_only"]
    search_fields = ["article_title", "article_author", "article_category", "article_tag", 'video_published', 'text_published']
    list_display = ["article_title", "article_author", "article_category", 'video_published', 'text_published', "video_only", "written_only", 'pic_slug']
    list_editable = ['video_published', 'text_published', "video_only", "written_only"]


class  CategoryAdmin(admin.ModelAdmin):
      fields = ['name', 'category_title', 'parent']


class  AuthorAdmin(admin.ModelAdmin):
      list_display = ['name', 'pic_slug']      
            


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
