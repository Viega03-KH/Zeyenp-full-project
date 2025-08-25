from django.contrib import admin
from .models import Category, GalleryContent

@admin.register(GalleryContent)
class GalleryContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image', 'id')
    search_fields = ('title', 'subtitle')
    list_filter = ('category',)
    list_per_page = 20
    fieldsets = (
        ('КАТЕГОРИЯ И ИЗОБРАЖЕНИЕ', {
            'classes': ('collapse',),
            'fields': ('category', 'image'),
        }),
        ('ЗАГОЛОВОК ПОДЗАГОЛОВОК [UZ]', {
            'classes': ('collapse',),
            'fields': ('title_uz', 'subtitle_uz'),
        }),
        ('ЗАГОЛОВОК ПОДЗАГОЛОВОК [EN]', {
            'classes': ('collapse',),
            'fields': ('title_en', 'subtitle_en'),
        }),
        ('ЗАГОЛОВОК ПОДЗАГОЛОВОК [RU]', {
            'classes': ('collapse',),
            'fields': ('title_ru', 'subtitle_ru'),
        }),
        ('ЗАГОЛОВОК ПОДЗАГОЛОВОК [TR]', {
            'classes': ('collapse',),
            'fields': ('title_tr', 'subtitle_tr'),
        }),
    )



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')             
    search_fields = ('name',)                
    list_per_page = 20       
    
    fieldsets = (
    ('TITLE', {
        'classes': ('collapse',),
        'fields': ['name_uz', 'name_ru', 'name_en', 'name_tr', 'image']
    }),
    )