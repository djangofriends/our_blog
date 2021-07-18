from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blog/templates/index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        context_object_name = 'article_list'
        return Article.objects.order_by('-pub_date')[:10]