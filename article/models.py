from django.db import models
from ckeditor.fields import RichTextField
from django.contrib import auth
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length= 50,verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank = True,null=True,verbose_name="Makale görüntü ekleyin")
    
    objects=models.Manager()
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-created_date"]
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name = "Makale",related_name="comments" )
    comment_author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    comment_content = models.CharField(max_length=200,verbose_name="Yorumunu Yaz")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ["-comment_date"]