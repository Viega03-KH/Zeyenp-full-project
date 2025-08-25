from django.shortcuts import render, redirect
from news_app.models import NewsContent
from gallery_app.models import GalleryContent
from django.contrib import messages
from .models import Contact

def home_page(request):
    news_list = NewsContent.objects.order_by('-id')[:5]
    gallery_list = GalleryContent.objects.order_by('-id')
    
    context = {
        'news_list': news_list,
        'gallery_list': gallery_list,
        }
    return render(request, 'pages/page-home.html', context )




def about_page(request):
    news_list = NewsContent.objects.order_by('-id')[:5]
    gallery_list = GalleryContent.objects.order_by('-id')[:8]
    
    context = {
        'news_list': news_list,
        'gallery_list': gallery_list,
        }
    return render(request, 'pages/page-about.html', context )



def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # oddiy validatsiya
        if not name or not email or not subject or not message:
            messages.error(request, "All fields are required!")
        else:
            # DB ga yozish
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact_page")  # qayta yuklash uchun

    return render(request, "pages/page-contact.html")