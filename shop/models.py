from django.db import models

class Item(models.Model):
    #    item_id = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='item_images/%Y/%m', blank=True)
    price = models.FloatField(max_length=9, null=True, blank=True)
    pub_date = models.DateTimeField('date added')
    def __unicode__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=15)  
    def __unicode__(self):
        return self.name

class Basket(models.Model):
    item = models.ManyToManyField(Item)
    total_price = models.FloatField(max_length=9)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.user

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='item_images/%Y/%m', blank=True)        
    link = models.URLField(blank=True)
    pub_date = models.DateTimeField('date added', blank=True)
    def __unicode__(self):
        return self.link

class Site(models.Model):
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title
    
class Paragraph(models.Model):
    site = models.ForeignKey(Site)
    heading = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=5000)
    def __unicode__(self):
        return self.content
    
class Image(models.Model):
    site = models.ForeignKey(Site)
    image = models.ImageField(upload_to='item_images/%Y/%m')
    alt = models.CharField(max_length=200)
    caption = models.CharField(max_length=200, blank = True)
    def __unicode__(self):
        return self.image
    
