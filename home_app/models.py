from django.db import models

class HomeContent(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='home/HomeContent')
    class Meta:
        verbose_name = 'Главная контент'
    def __str__(self):
        return self.title
    

class TestimonialsContent(models.Model):
    full_name = models.CharField(max_length=200)
    commint = models.TextField()
    author = models.ImageField(upload_to='home/TestimonialsContent')
    
    class Meta:
        verbose_name = 'Рекомендация контент'
    def __str__(self):
        return self.full_name
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} - {self.subject}"