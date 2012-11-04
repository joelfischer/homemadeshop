from shop.models import Item, News, Site, Paragraph, models
from django.contrib import admin
from django.forms import TextInput, Textarea

class ParaInline(admin.StackedInline):
    model = Paragraph
    extra = 1

class HomemadeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':60})},
    }
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Heading', {'fields': ['heading']}),
    ]
    inlines = [ParaInline]

admin.site.register(Site, HomemadeAdmin)
admin.site.register(Item)
admin.site.register(News)

