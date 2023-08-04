from django.db import models #модель

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True) #модель


    def __str__(self):
        return self.name #отображаем название статей через имя