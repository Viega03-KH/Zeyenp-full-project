from django.shortcuts import render, get_object_or_404
from .models import GalleryContent, Category


def gallery_page(request):
    gallery_list = GalleryContent.objects.order_by('-id')[:10]
    
    context = {
        'gallery_list': gallery_list,
        }
    return render(request, 'pages/page-gallery.html', context )

def single_page(request, id):
    category = get_object_or_404(Category, id=id)
    gallery_list = GalleryContent.objects.filter(category=category).order_by('-id')
    
    context = {
        'gallery_list': gallery_list,
        }
    return render(request, 'pages/page-single.html', context )


def collection_page(request):
    collection_list = Category.objects.order_by('-id')
    
    context = {
        'collection_list': collection_list,
        }
    return render(request, 'pages/page-collection.html', context )