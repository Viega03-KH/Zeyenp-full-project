from django.db import models
from PIL import Image
import os

class Category(models.Model):
    name = models.CharField('Заголовок', max_length=100)
    image = models.ImageField('изображение', upload_to='gallery/Gallerycategory', null=True, blank=True)
    class Meta:
        verbose_name = 'Коллекци'

    def __str__(self):
        return self.name


import os
from PIL import Image
from django.db import models

class GalleryContent(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Коллекци")
    title = models.CharField('Заголовок', max_length=200, null=True, blank=True)
    subtitle = models.TextField('контент', default='GalleryContent subtitle', null=True, blank=True)
    image = models.ImageField('изображение', upload_to='gallery/GalleryContent')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Галерея контент'

    def __str__(self):
        return self.title.strip() if self.title and self.title.strip() else "безымянный"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            # Maksimal o'lchamni belgilash
            max_size = (1280, 900)
            img.thumbnail(max_size, Image.LANCZOS)

            # Fayl kengaytmasini olish
            ext = os.path.splitext(img_path)[1].lower()

            # JPEG optimizatsiya
            if ext in ['.jpg', '.jpeg']:
                img = img.convert("RGB")  # Rang profilini moslashtirish
                img.save(img_path, format='JPEG', quality=88, optimize=True, progressive=True)

            # PNG optimizatsiya
            elif ext == '.png':
                img.save(img_path, format='PNG', optimize=True)

            # WebP formatida ham saqlash imkoniyati
            # webp_path = img_path.rsplit('.', 1)[0] + '.webp'
            # img.save(webp_path, format='WEBP', quality=85, method=6)

