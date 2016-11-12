from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'shop.views.site', {'site': 'START'}),
    url(r'^home/$', 'shop.views.index'),
    url(r'^hockley/$', 'shop.views.index'),
    url(r'^menu/$', 'shop.views.site', {'site': 'MENU'}),
#    url(r'^shop/$', 'shop.views.shop'),
    url(r'^blog/$', 'shop.views.blog'),
    url(r'^jobs/$', 'shop.views.site', {'site': 'JOBS'}),
    url(r'^friends/$', 'shop.views.site', {'site': 'FRIENDS'}),
    url(r'^find_us/$', 'shop.views.site', {'site': 'FIND_US'}),
    url(r'^contact/$', 'shop.views.contact'),
    url(r'^suppliers/$', 'shop.views.site', {'site': 'SUPPLIERS'}),
    url(r'^cakes/$', 'shop.views.gallery', {'site': 'CAKES'}),
     url(r'^gallery/$', 'shop.views.gallery', {'site': 'GALLERY'}),
    url(r'^cakes/item/(?P<item_id>\d+)/$', 'shop.views.cake_detail'),
    url(r'^gallery/item/(?P<item_id>\d+)/$', 'shop.views.image_detail'),
#    url(r'^shop/item/(?P<item_id>\d+)/$', 'shop.views.detail'),
#    url(r'^shop/basket/(?P<basket_id>\d+)/$', 'shop.views.basket'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    
    url(r'^sherwood/$', 'shop.views.site', {'site': 'SHERWOOD_HOME'}),
    url(r'^sherwood_menu/$', 'shop.views.site', {'site': 'SHERWOOD_MENU'}),
    
    url(r'^catering/$', 'shop.views.site', {'site': 'CATERING_HOME'}),
    url(r'^weddings/$', 'shop.views.site', {'site': 'WEDDINGS'}),
    url(r'^parties/$', 'shop.views.site', {'site': 'PARTIES'}),
    url(r'^events/$', 'shop.views.site', {'site': 'EVENTS'}),
    url(r'^pavilion/$', 'shop.views.site', {'site': 'PAVILION_HOME'}),

#    # Examples:
#    url(r'^$', 'homemadeshop.views.home', name='home'),
#    url(r'^homemadeshop/', include('homemadeshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^shop/admin/', include(admin.site.urls)),
#    url(r'^', include('cms.urls')),
)

#if settings.DEBUG:
#    urlpatterns = patterns('',
#    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#    url(r'', include('django.contrib.staticfiles.urls')),
#) + urlpatterns
