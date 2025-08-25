from django.contrib import admin
from .models import HomeContent, TestimonialsContent, Contact

admin.site.site_header = "Zeynap"
admin.site.site_title = "Zeynap Admin"
admin.site.index_title = "Boshqaruv paneliga xush kelibsiz"

@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_per_page = 20

    fieldsets = (
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

@admin.register(TestimonialsContent)
class TestimonialsContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'commint')
    search_fields = ('full_name',)
    list_per_page = 20

    fieldsets = (
    ('ПОЛНОЕ ИМЯ', {
        'classes': ('collapse',),
        'fields': ('full_name',)
    }),
    ('КОММЕНТАРИЙ [UZ]', {
        'classes': ('collapse',),
        'fields': ('commint_uz',)
    }),
    ('КОММЕНТАРИЙ [RU]', {
        'classes': ('collapse',),
        'fields': ('commint_ru',)
    }),
    ('КОММЕНТАРИЙ [EN]', {
        'classes': ('collapse',),
        'fields': ('commint_en',)
    }),
    ('КОММЕНТАРИЙ [TR]', {
        'classes': ('collapse',),
        'fields': ('commint_tr',)
    }),
)


# admin.py
from django.contrib.admin import AdminSite
from django.utils import timezone

class MyAdminSite(AdminSite):
    site_header = "Mening Admin Panelim"

    def index(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['test_number'] = 12345
        return super().index(request, extra_context=extra_context)

admin_site = MyAdminSite(name="myadmin")


@admin.register(Contact)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")  # admin listida ko‘rinadigan ustunlar
    readonly_fields = ("name", "email", "subject", "message", "created_at")  # faqat o‘qish uchun

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False