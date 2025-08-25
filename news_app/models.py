from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
import os

class Category(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'категория'
    def __str__(self):
        return self.name


class NewsContent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = RichTextUploadingField()
    image = models.ImageField(upload_to='news/NewsContent')
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)     

    class Meta:
        verbose_name = 'Новости контент'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            max_size = (1280, 900)  # maksimal ruxsat etilgan o‘lcham

            if img.height > max_size[1] or img.width > max_size[0]:
                img.thumbnail(max_size)  # proporsiyani saqlab kichraytiradi
                img.save(img_path, optimize=True, quality=85)


