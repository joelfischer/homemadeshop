from django.db import models
from django import forms

#class Item(models.Model):
#    #    item_id = models.IntegerField()
#    title = models.CharField(max_length=200)
#    description = models.CharField(max_length=1000, blank=True)
#    image = models.ImageField(upload_to='item_images/%Y/%m', blank=True)
#    price = models.FloatField(max_length=9, null=True, blank=True)
#    pub_date = models.DateTimeField('date added')
#    def __unicode__(self):
#        return self.title

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    sender = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=12, required=True)
    subject = forms.CharField(max_length=100, required=False)
    cc_myself = forms.BooleanField(required=False)
    message = forms.CharField()

class Cake(models.Model):
    #    item_id = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='item_images/%Y/%m', blank=True)
    def __unicode__(self):
        return self.title

#class User(models.Model):
#    name = models.CharField(max_length=15)  
#    def __unicode__(self):
#        return self.name

#class Basket(models.Model):
#    item = models.ManyToManyField(Item)
#    total_price = models.FloatField(max_length=9)
#    user = models.ForeignKey(User)
#    def __unicode__(self):
#        return self.user

#class News(models.Model):
#    title = models.CharField(max_length=200)
#    description = models.CharField(max_length=1000, blank=True)
#    image = models.ImageField(upload_to='item_images/%Y/%m', blank=True)        
#    link = models.URLField(blank=True)
#    pub_date = models.DateTimeField('date added', blank=True)
#    def __unicode__(self):
#        return self.link
    
class Page(models.Model):    
    TITLE_CHOICES = (
                    (u'START',u'START'),
                    (u'HOME',u'HOME'),
                    (u'MENU',u'MENU'),
                    (u'GALLERY',u'GALLERY'),
                    (u'PARTIES',u'PARTIES'),
                    (u'CAKES',u'CAKES'),
                    (u'GALLERY',u'GALLERY'),
                    (u'EVENTS',u'EVENTS'),
                    (u'CHRISTMAS',u'CHRISTMAS'),
                    (u'SUPPLIERS',u'SUPPLIERS'),
                    (u'FIND_US',u'FIND US'), 
                    (u'JOBS',u'JOBS'),
                    (u'CONTACT_US',u'CONTACT US'),
                    (u'FRIENDS',u'FRIENDS'),
                    (u'BLOG',u'BLOG'),
                    (u'CATERING_HOME',u'CATERING HOME'),
                    (u'WEDDINGS',u'WEDDINGS'),
                    (u'PAVILION_HOME',u'PAVILION HOME'),
                     )
    title = models.CharField(max_length=20, choices=TITLE_CHOICES)
    heading = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title
    
#class Layout(models.Model):
#    site = models.OneToOneField(Page)
#    TYPE_CHOICES = (
#                    (u'1COL',u'1 Column'),
#                    (u'2COL',u'2 Columns'),
#                    (u'3COL',u'3 Columns'),
#                    (u'2ROW',u'2 Rows'),
#                    (u'3ROW',u'2 Rows'),
#                    )
#    type = models.CharField(max_length=4,choices=TYPE_CHOICES)
#    def __unicode__(self):
#        return self.type
    
class Paragraph(models.Model):
    page = models.ForeignKey(Page)
    heading = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=5000)
    def __unicode__(self):
        return self.content
    
class Image(models.Model):
    page = models.ForeignKey(Page)
    image = models.ImageField(upload_to='item_images/%Y/%m')
    alt = models.CharField(max_length=200)
    caption = models.CharField(max_length=200, blank = True)
    def __unicode__(self):
        return self.image.name
    
class Pdf(models.Model):
    page = models.ForeignKey(Page)
    pdf = models.FileField(upload_to='pdfs/%Y/%m')
    title = models.CharField(max_length=200, blank=True)
    def __unicode__(self):
        return self.pdf.name

class ImageSlider(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class SliderImage(models.Model):
    slider = models.ForeignKey(ImageSlider)
    image = models.ImageField(upload_to='item_images/%Y/%m')
    alt = models.CharField(max_length=200)
    caption = models.CharField(max_length=200, blank = True)
    def __unicode__(self):
        return self.image.name
    
class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date added')
    news_item = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title
    
class Blog_Paragraph(models.Model):
    blog = models.ForeignKey(Blogpost)
    heading = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=5000)
    def __unicode__(self):
        return self.content
    
class Blog_Image(models.Model):
    blog = models.ForeignKey(Blogpost)
    image = models.ImageField(upload_to='item_images/%Y/%m')
    alt = models.CharField(max_length=200)
    caption = models.CharField(max_length=200, blank = True)
    def __unicode__(self):
        return self.image.name
    
class Blog_Link(models.Model):
    blog = models.ForeignKey(Blogpost)
    link = models.URLField(blank=True)
    def __unicode__(self):
        return self.link
    

    
    
    


    
