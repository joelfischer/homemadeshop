from shop.models import Page, Paragraph, Blog_Paragraph, models, Image, Blog_Image, Blog_Link, ImageSlider, SliderImage, Cake, Blogpost, Pdf
from django.contrib import admin
from django.forms import TextInput, Textarea

class ParaInline(admin.StackedInline):
    model = Paragraph
    extra = 1
    
class ImageInline(admin.StackedInline):
    model = Image
    extra = 1 
    
class PdfInline(admin.StackedInline):
    model = Pdf
    extra = 1
    
class SliderImageInline(admin.StackedInline):
    model = SliderImage
    extra = 1
    
class BlogParaInline(admin.StackedInline):
    model = Blog_Paragraph
    extra = 1
    
class BlogImageInline(admin.StackedInline):
    model = Blog_Image
    extra = 1 

class BlogLinkInline(admin.StackedInline):
    model = Blog_Link
    extra = 1 

class HomemadeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':40})},
    }
    fieldsets = [
        (None,      {'fields': ['title']}),
        ('Heading', {'fields': ['heading']}),
    ]
    inlines = [ParaInline,ImageInline,PdfInline]
    
class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderImageInline]
    
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':40})},
    }
    fieldsets = [
        (None,      {'fields': ['title']}),
        ('Show in news side bar (short preview)?',      {'fields': ['news_item']}),
        (None,      {'fields': ['pub_date']}),
    ]
    inlines = [BlogParaInline,BlogImageInline,BlogLinkInline]

admin.site.register(Page, HomemadeAdmin)
admin.site.register(Cake)
admin.site.register(Image)
admin.site.register(Blogpost, BlogAdmin)
admin.site.register(ImageSlider, SliderAdmin)

