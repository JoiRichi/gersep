from django.shortcuts import render
from .models import NewsFeed
from django.utils import timezone

def index_page(request):
    news = NewsFeed.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'homeapp/index.html', {'news': news} )
# Create your views here.