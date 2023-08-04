from hexlet_django_blog.article.models import Article
from django.forms import ModelForm


class ArticleForm(ModelForm): #форма
    class Meta:
        model = Article
        fields = ['name', 'body']