from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewDetail


urlpatterns = [
   path('', NewsList.as_view(), name='news'),
   path('<int:pk>', NewDetail.as_view()),
]
