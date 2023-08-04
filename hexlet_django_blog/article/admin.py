from django.contrib import admin

# Register your models here.
from .models import Article #добавили модель Article
from django.contrib.admin import DateFieldListFilter


@admin.register(Article) #добавили модель Article
class ArticleAdmin(admin.ModelAdmin): #для отображения статей
    list_display = ('name', 'timestamp') # Перечисляем поля, отображаемые в таблице списка статей
    search_fields = ['name', 'body']
    list_filter = (('timestamp', DateFieldListFilter),) # Перечисляем поля для фильтрации
