# -*- coding: utf-8 -*-
from django.core.checks import Tags
from django.db import models


class Category(models.Model):
    cname=models.CharField(max_length=128,unique=True,verbose_name='类别名称')

    class Meta:
        db_table ='t_category'
        verbose_name_plural = '类别'
    def __repr__(self):
        return "%s"%self.cname
class Tags(models.Model):
        tname = models.CharField(max_length=32,unique=True,verbose_name='标签名称')

        class Meta:
            db_table = 't_tags'
            verbose_name_plural = '标签'
        def __repr__(self):
            return "%s" % self.tname
class Post(models.Model):
    title = models.CharField(max_length=128,unique=True)
    desc = models.TextField()
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = '帖子'

    def __repr__(self):
        return "%s" % self.title
