from django.urls import path
from .views import ArticleView


app_name = "articles"

urlpatterns = [
    path('btc_checker/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view())
    ]