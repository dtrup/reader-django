from django.db import models
from django.urls import reverse


class Text(models.Model):
    text_id = models.CharField(max_length=100,primary_key=True)
    text_order = models.PositiveSmallIntegerField(default=1)
    collection = models.CharField(max_length=100, null=True,blank=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100, blank=True)
    languages = models.CharField(max_length=100, blank=True)
    number_chapters = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ('text_id',)
        verbose_name = 'text'
        verbose_name_plural = 'texts'

    def __str__(self):
        return self.text_id



class Sentence(models.Model):
    sentence_id = models.AutoField(primary_key=True)
    sentence_inner_id = models.CharField(max_length=64,blank=True,null=True)
    text_id = models.ForeignKey(Text,
                                related_name='sentences',
                                on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=300, null=True,blank=True)
    chapter_number = models.PositiveSmallIntegerField(default=1)

    en = models.TextField(blank=True,null=True)
    es = models.TextField(blank=True,null=True)
    pt = models.TextField(blank=True,null=True)
    fr = models.TextField(blank=True,null=True)
    it = models.TextField(blank=True,null=True)
    de = models.TextField(blank=True,null=True)
    ro = models.TextField(blank=True,null=True)
    hu = models.TextField(blank=True,null=True)
    nl = models.TextField(blank=True,null=True)
    da = models.TextField(blank=True,null=True)
    id = models.TextField(blank=True,null=True)


    class Meta:
        ordering = ('id',)
        index_together = (('id', 'text_id'),)

    def __str__(self):
        return self.en





