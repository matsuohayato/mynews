
# Register your models here.
from django.contrib import admin
from .models import Article,Category

class AricleAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
admin.site.register(Article, AricleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
admin.site.register(Category, CategoryAdmin)

