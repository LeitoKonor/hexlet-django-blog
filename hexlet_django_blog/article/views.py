from django.shortcuts import render, get_object_or_404, redirect #новое приложение
from django.views import View
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm


class IndexView(View): #статьи

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })
    

class ArticleView(View): #конкретная статья

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View): #создание статьи

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('/articles/') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form}) #форма
    

class ArticleFormEditView(View): #редактировать статью

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
            article_id = kwargs.get('id')
            article = Article.objects.get(id=article_id)
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('/articles/')
            return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})
    

class ArticleFormDeleteView(View): #удалить статью

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('/articles/')


#новое приложение

# Create your views here.
