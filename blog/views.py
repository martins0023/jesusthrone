from django.shortcuts import render
from home.models import projects, minister
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Blog
from home.models import  program, minister, projects, BackgroundImageHomeSlider, Church_info
from pages.forms import Subscribers
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import Make_request
#def blog(request):
#    context = {
#        'title': 'Blog',
#        'the_title': 'Our Blog',
        
#    }
#    return render(request,  'blog/blog.html', context)

class BlogListView(ListView):        
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['form_subscibe'] = 'form_subscibe',
        context['title'] = 'Blog'
        context['the_title'] = 'Our Blog'
        context['background'] = BackgroundImageHomeSlider.objects.all()
        context['church_infos'] = Church_info.objects.all()
        return context
    
    
    
class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blogs'
    
    def user_comment(request):
        
        
        if request.method == 'POST':
            user_com = Make_request(request.POST)
        if user_com.is_valid():
            user_com.save()
        
            messages.success(request, f'Your comment has been posted successfully, reload the page. Thanks !')
            return redirect('home')
        else:
            user_com = Make_request()
        comment_context = super().get_context_data(request)
        comment_context['user_com'] = 'user_com'
        
        return comment_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['the_title'] = 'Blog Details'
        context['background'] = BackgroundImageHomeSlider.objects.all()
        context['church_infos'] = Church_info.objects.all()
        return context

#class PostDetailView(DetailView):
#    model = Post
    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['title'] = ''
#        context['links'] = Link.objects.all()
#        context['org_info'] = Org_info.objects.all()
#        return context