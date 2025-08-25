from modeltranslation.translator import register, TranslationOptions
from .models import NewsContent, Category

@register(NewsContent)
class NewsContentTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle',) 

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', ) 
