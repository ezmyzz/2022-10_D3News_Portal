from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    model = News
    ordering = '-some_datetime'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['time_now'] = datetime.utcnow() заменяем тегом
        context['new_post'] = None
        return context


class NewDetail(DetailView):
    model = News
    template_name = 'new.html'
    context_object_name = 'new'
