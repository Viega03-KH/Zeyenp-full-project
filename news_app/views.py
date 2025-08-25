from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from gallery_app.models import GalleryContent
from .models import NewsContent, Category

def news_page(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category')  # URL query param: ?category=3

    news_qs = NewsContent.objects.all().order_by('-id')

    # qidiruv bo‘lsa
    if query:
        news_qs = news_qs.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    # kategoriya bo‘yicha filter
    if category_id:
        news_qs = news_qs.filter(category_id=category_id)

    # pagination
    paginator = Paginator(news_qs, 5)
    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)

    category_list = Category.objects.all()
    gallery_list = GalleryContent.objects.order_by('-id')[:10]

    context = {
        'news_list': news_list,
        'gallery_list': gallery_list,
        'category_list': category_list,
        'query': query,
        'category_id': category_id
    }
    return render(request, 'pages/page-news.html', context)


def news_single_page(request, id): 
    news_list =get_object_or_404(NewsContent, id=id)
    
    context = {
        'news_list': news_list,
        }
    return render(request, 'pages/page_news_single.html', context )