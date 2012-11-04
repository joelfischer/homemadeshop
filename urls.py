from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/$', 'shop.views.index'),
    url(r'^shop/$', 'shop.views.shop'),
    url(r'^shop/item/(?P<item_id>\d+)/$', 'shop.views.detail'),
    url(r'^shop/basket/(?P<basket_id>\d+)/$', 'shop.views.basket'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    # Examples:
#    url(r'^$', 'homemadeshop.views.home', name='home'),
#    url(r'^homemadeshop/', include('homemadeshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shop/admin/', include(admin.site.urls)),
    url(r'^$', 'shop.views.index'),
)
