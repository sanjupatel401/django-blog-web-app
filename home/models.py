from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .slugy import *
# Create your models here.

class categoies(models.Model):
    cate_name=models.CharField(max_length=30)


class BlogModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,blank=False)
    content=FroalaField(theme='dark')
    slug=models.SlugField(max_length=30)
    image=models.ImageField(upload_to='thumbnail',blank=False)
    create_to=models.DateField(auto_now=True)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)





# class add_blog(models.Model):
#     title=models.CharField(max_length=300,null=False,blank=False)
#     content=FroalaField();
#     date=models.DateField(auto_now=True)
#     category=models.ForeignKey(categoies,on_delete=models.CASCADE);   