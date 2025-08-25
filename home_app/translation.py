from modeltranslation.translator import register, TranslationOptions
from .models import HomeContent, TestimonialsContent

@register(HomeContent)
class HomeContentTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle',) 

@register(TestimonialsContent)
class TestimonialsContentTranslationOptions(TranslationOptions):
    fields = ('full_name', 'commint') 
