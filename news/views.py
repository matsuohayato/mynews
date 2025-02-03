from django.views.generic import TemplateView, ListView
# Create your views here.
from django.shortcuts import render
from .models import Article
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ArticleForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import PhotoPost

class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'object_list'

    queryset = Article.objects.all().order_by('-id')

    paginate_by =9

class weatherView(TemplateView):
    template_name='weather.html'

class sportsView(TemplateView):
    template_name='sports.html'

class livingView(TemplateView):
    template_name='living.html'

class politicsView(TemplateView):
    template_name='politics.html'

class businessView(TemplateView):
    template_name='business.html'

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    template_name = 'post_photo.html'
    form_class = ArticleForm
    
    success_url = reverse_lazy('news:post_done')
    
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
