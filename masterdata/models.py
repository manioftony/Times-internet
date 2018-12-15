from __future__ import unicode_literals

from django.db import models

# Create your models here.



ACTIVE = ((0,'Inactive'), (2, 'Active'),)
class Base(models.Model):
    
    """ Basic Fields """

    is_active = models.PositiveIntegerField(choices = ACTIVE, default=2)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)

    def switch(self):
        self.is_active = {0: 2, 2: 0}[self.is_active]
        self.save()
        return self.is_active

    class Meta:
        abstract = True





class Category(Base):
    name = models.CharField(max_length=200,blank=True, null=True)
    parent = models.CharField(max_length=200,blank=True, null=True)
    is_featured  = models.BooleanField(default=True)
    image = models.ImageField(blank=True,null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    def __unicode__(self):
        return self.name





