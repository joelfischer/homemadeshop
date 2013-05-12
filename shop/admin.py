from shop.models import Item, News, Site, Paragraph, models, Image, Layout, ImageSlider, SliderImage
from django.contrib import admin
from django.forms import TextInput, Textarea

class LayoutInline(admin.StackedInline):
    model = Layout

class ParaInline(admin.StackedInline):
    model = Paragraph
    extra = 1
    
class ImageInline(admin.StackedInline):
    model = Image
    extra = 1 
    
class SliderImageInline(admin.StackedInline):
    model = SliderImage
    extra = 1

class HomemadeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':60})},
    }
    fieldsets = [
        (None,      {'fields': ['title']}),
        ('Heading', {'fields': ['heading']}),
    ]
    inlines = [LayoutInline,ParaInline,ImageInline]
    
class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderImageInline]

admin.site.register(Site, HomemadeAdmin)
admin.site.register(Item)
admin.site.register(News)
admin.site.register(ImageSlider, SliderAdmin)

