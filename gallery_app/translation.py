from modeltranslation.translator import register, TranslationOptions
from .models import GalleryContent, Category

@register(GalleryContent)
class GalleryContentTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle',) 

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',) 
