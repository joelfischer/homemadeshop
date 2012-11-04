from django.http import HttpResponse
from django.shortcuts import render_to_response
from shop.models import Item, Basket, News, Site, Paragraph
from django.http import Http404
from django.template import RequestContext



def shop(request):
#    return HttpResponse("Hello, world. You're at the shop index.")
    latest_item_list = Item.objects.all().order_by('-pub_date')[:5]
    latest_news_list = News.objects.all().order_by('-pub_date')[:5]
    values = {'latest_item_list': latest_item_list, 'latest_news_list': latest_news_list}
    return render_to_response('shop/shop.html', values, context_instance=RequestContext(request))

def index(request):
    page = Site.objects.get(title="HOME") 
    paras = Paragraph.objects.filter(site_id__exact=page.pk)
    latest_news_list = News.objects.all().order_by('-pub_date')[:5]
    values = {'page': page, 'paras':paras, 'latest_news_list': latest_news_list}
    return render_to_response('shop/index.html', values, context_instance=RequestContext(request))


def detail(request, item_id):
#    return HttpResponse("You're looking at item %s." % item_id)
    try:
        i = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404
    latest_news_list = News.objects.all().order_by('-pub_date')[:5]
    values = {'item': i, 'latest_news_list': latest_news_list}
    return render_to_response('shop/detail.html', values, context_instance=RequestContext(request))

def basket(request, basket_id):
    return HttpResponse("You're looking at basket %s." % basket_id)