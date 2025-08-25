from django.contrib import admin
from .models import NewsContent, Category


@admin.register(NewsContent)
class NewsContentAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'created_at', 'updated_at', 'id', )
    search_fields = ('title', 'subtitle')
    list_filter = ('category',)
    list_per_page = 20
    fieldsets = (
        ('Контент', {
            'classes': ('collapse',),
            'fields': ('category', 'image',)
        }),
        
        ('Заголовок [UZ]', {
            'classes': ('collapse',),
            'fields': ('title_uz', 'subtitle_uz')
        }),
        
        ('Заголовок [RU]', {
            'classes': ('collapse',),
            'fields': ('title_ru', 'subtitle_ru')
        }),
        
        ('Заголовок [EN]', {
            'classes': ('collapse',),
            'fields': ('title_en', 'subtitle_en')
        }),
        
        ('Заголовок [TR]', {
            'classes': ('collapse',),
            'fields': ('title_tr', 'subtitle_tr')
        }),
    )





@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)             
    search_fields = ('name',)                
    list_per_page = 20       
    
    fieldsets = (
    ('ЗАГОЛОВОК [UZ]', {
        'classes': ('collapse',),
        'fields': ['name_uz']
    }),
    ('ЗАГОЛОВОК [RU]', {
        'classes': ('collapse',),
        'fields': ['name_ru']
    }),
    ('ЗАГОЛОВОК [EN]', {
        'classes': ('collapse',),
        'fields': ['name_en']
    }),
    ('ЗАГОЛОВОК [TR]', {
        'classes': ('collapse',),
        'fields': ['name_tr']
    }),
)
