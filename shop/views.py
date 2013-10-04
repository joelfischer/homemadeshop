from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from shop.models import Page, Paragraph, Blog_Paragraph, Image, Blog_Image, Blog_Link, SliderImage, Cake, Blogpost, ContactForm
from django.http import Http404
from django.template import RequestContext
from django.core.mail import send_mail

def contact(request):
    page = Page.objects.get(title='CONTACT_US')
    paras = Paragraph.objects.filter(page_id__exact=page.pk)
    images = Image.objects.filter(page_id__exact=page.pk) 
    news = getNews()
    
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            message = 'From: '+name+ '\n Email: '+sender+ '\n Phone number: '+phone_number + '\n Message: '+message
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['joelefischer@gmail.com']
            if cc_myself:
                recipients.append(sender)
                send_mail(subject, message, sender, recipients)
            form = ContactForm()
            values = {'page': page, 'paras':paras, 'images':images, 'news': news, 'form': form, 'success': True}
            return render_to_response('shop/contact.html', values, context_instance=RequestContext(request))
    else:
        form = ContactForm() # An unbound form
    values = {'page': page, 'paras':paras, 'images':images, 'news': news, 'form': form}
    return render_to_response('shop/contact.html', values, context_instance=RequestContext(request))
    
def start(request):
    return render_to_response('shop/start.html', context_instance=RequestContext(request))

#def shop(request):
#    return HttpResponse("Hello, world. You're at the shop index.")
#    latest_item_list = Item.objects.all().order_by('-pub_date')[:5]
#    latest_news_list = News.objects.all().order_by('-pub_date')[:5]
#    values = {'latest_item_list': latest_item_list, 'latest_news_list': latest_news_list}
#    return render_to_response('shop/shop.html', values, context_instance=RequestContext(request))

def getNews():
    posts = Blogpost.objects.all().filter(news_item=True).order_by('pub_date')
    for p in posts:
        if p.news_item == True: 
            p.images = Blog_Image.objects.filter(blog_id__exact=p.pk)[:1]
            p.links = Blog_Link.objects.filter(blog_id__exact=p.pk)[:1]
            p.paras = Blog_Paragraph.objects.filter(blog_id__exact=p.pk)[:1]
    return posts

def blog(request):
    news = getNews()
    posts = Blogpost.objects.all().order_by('pub_date')
    for p in posts:
        p.paras = Blog_Paragraph.objects.filter(blog_id__exact=p.pk)
        p.images = Blog_Image.objects.filter(blog_id__exact=p.pk)
        p.links = Blog_Link.objects.filter(blog_id__exact=p.pk)
    values = {'posts': posts, 'news': news}
    return render_to_response('shop/blog_home.html', values, context_instance=RequestContext(request))

def index(request):
    slider_images =  SliderImage.objects.all()
    try:
        page = Page.objects.get(title="HOME")
    except Exception as e:
        print e
    paras = Paragraph.objects.filter(page_id__exact=page.pk)
#    layout = Layout.objects.filter(site_id__exact=page.pk)
    news = getNews()
    values = {'page': page, 'paras':paras, 'news': news,'slider_images':slider_images}
    return render_to_response('shop/hockley_home.html', values, context_instance=RequestContext(request))

def site(request, site):
    slider_images =  SliderImage.objects.all()
    page = Page.objects.get(title=site)
    paras = Paragraph.objects.filter(page_id__exact=page.pk)
#    layout = Layout.objects.filter(site_id__exact=page.pk)
#    for l in layout:
#        layout_type = l.type
    images = Image.objects.filter(page_id__exact=page.pk) 
    paras_images = zip(images,paras) 
    news = getNews()
    values = {'page': page, 'paras_images': paras_images, 'paras':paras, 'images':images, 
              'slider_images':slider_images,'news': news}
    if site=='START':
        return render_to_response('shop/start_3COL.html', values, context_instance=RequestContext(request))
    if site=='MENU':
        return render_to_response('shop/menu.html', values, context_instance=RequestContext(request))
    elif site=='SHERWOOD_HOME':
        return render_to_response('shop/sherwood_home.html', values, context_instance=RequestContext(request))
    elif site=='SHERWOOD_MENU':
        return render_to_response('shop/sherwood_menu.html', values, context_instance=RequestContext(request))
    elif site=='CATERING_HOME':
        return render_to_response('shop/catering_home.html', values, context_instance=RequestContext(request))
    elif site=='WEDDINGS':
        return render_to_response('shop/catering_weddings.html', values, context_instance=RequestContext(request))
    elif site=='PARTIES':
        return render_to_response('shop/parties.html', values, context_instance=RequestContext(request))
    elif site=='EVENTS':
        return render_to_response('shop/events.html', values, context_instance=RequestContext(request))
    elif site=='JOBS':
        return render_to_response('shop/2COL.html', values, context_instance=RequestContext(request))
    elif site=='FIND_US':
        return render_to_response('shop/find_us.html', values, context_instance=RequestContext(request))
    elif site=='SUPPLIERS':
        return render_to_response('shop/2COL.html', values, context_instance=RequestContext(request))
    elif site=='FRIENDS':
        return render_to_response('shop/2COL.html', values, context_instance=RequestContext(request))
    else:
        return render_to_response('shop/start_3COL.html', values, context_instance=RequestContext(request))
    
def gallery(request, site):
    page = Page.objects.get(title=site)
    print page
    paras = Paragraph.objects.filter(page_id__exact=page.pk)
    news = getNews()
    if site == 'CAKES':
        cakes = Cake.objects.all()
        values = {'cakes': cakes, 'news': news, 'page': page, 'paras':paras}
        return render_to_response('shop/cakes.html', values, context_instance=RequestContext(request))
    elif site =='GALLERY':
        images = Image.objects.all()
#        images = Image.objects.all().filter(site_id__exact=page.pk)
        values = {'images': images, 'news': news, 'page': page, 'paras':paras}
        return render_to_response('shop/gallery.html', values, context_instance=RequestContext(request))

def cake_detail(request, item_id):
#    return HttpResponse("You're looking at item %s." % item_id)
    try:
        i = Cake.objects.get(pk=item_id)
    except Cake.DoesNotExist:
        raise Http404
    news = getNews()
    values = {'item': i, 'news': news}
    return render_to_response('shop/cake_detail.html', values, context_instance=RequestContext(request))

def image_detail(request, item_id):
#    return HttpResponse("You're looking at item %s." % item_id)
    try:
        i = Image.objects.get(pk=item_id)
    except Image.DoesNotExist:
        raise Http404
    news = getNews()
    values = {'item': i, 'news': news}
    return render_to_response('shop/image_detail.html', values, context_instance=RequestContext(request))

#def detail(request, item_id):
##    return HttpResponse("You're looking at item %s." % item_id)
#    try:
#        i = Item.objects.get(pk=item_id)
#    except Item.DoesNotExist:
#        raise Http404
#    latest_news_list = News.objects.all().order_by('-pub_date')[:5]
#    values = {'item': i, 'latest_news_list': latest_news_list}
#    return render_to_response('shop/detail.html', values, context_instance=RequestContext(request))
#
#def basket(request, basket_id):
#    return HttpResponse("You're looking at basket %s." % basket_id)