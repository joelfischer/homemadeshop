from django.http import HttpResponse
from django.shortcuts import render_to_response
from shop.models import Item, Basket, News, Site, Paragraph, Layout, Image, SliderImage
from django.http import Http404
from django.template import RequestContext


def start(request):
    return render_to_response('shop/start.html', context_instance=RequestContext(request))

def shop(request):
#    return HttpResponse("Hello, world. You're at the shop index.")
    latest_item_list = Item.objects.all().order_by('-pub_date')[:5]
    latest_news_list = News.objects.all().order_by('-pub_date')[:5]
    values = {'latest_item_list': latest_item_list, 'latest_news_list': latest_news_list}
    return render_to_response('shop/shop.html', values, context_instance=RequestContext(request))

def index(request):
    slider_images =  SliderImage.objects.all()
    try:
        page = Site.objects.get(title="HOME")
    except Exception as e:
        print e
    paras = Paragraph.objects.filter(site_id__exact=page.pk)
    layout = Layout.objects.filter(site_id__exact=page.pk)
    latest_news_list = News.objects.all().order_by('-pub_date')[:5]
    values = {'page': page, 'paras':paras, 'latest_news_list': latest_news_list,'slider_images':slider_images}
    return render_to_response('shop/index.html', values, context_instance=RequestContext(request))

def site(request, site):
    print site
    slider_images =  SliderImage.objects.all()
    page = Site.objects.get(title=site)
    paras = Paragraph.objects.filter(site_id__exact=page.pk)
    layout = Layout.objects.filter(site_id__exact=page.pk)
    for l in layout:
        layout_type = l.type
    images = Image.objects.filter(site_id__exact=page.pk) 
    paras_images = zip(images,paras) 
    latest_news_list = News.objects.all().order_by('-pub_date')[:5]
    values = {'page': page, 'paras_images': paras_images, 'paras':paras, 'images':images, 
              'slider_images':slider_images,'latest_news_list': latest_news_list}
    if site=='START':
        print 'yup'
        return render_to_response('shop/start_3COL.html', values, context_instance=RequestContext(request))
    else:
        return render_to_response('shop/'+layout_type+'.html', values, context_instance=RequestContext(request))


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