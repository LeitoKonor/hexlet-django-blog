from django.urls import path #создали

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view()), #статьи
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='articles_update'), #редактировать статью (обязательно до статьи)
    path('<int:id>/delete/', views.ArticleFormDeleteView.as_view(), name='articles_delete'), #удалить статью
    path('<int:id>/', views.ArticleView.as_view()), #статья
    path('create/', views.ArticleFormCreateView.as_view(), name='articles_create'), #создать статью
] #создали
