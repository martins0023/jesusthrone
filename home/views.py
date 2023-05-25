from django.shortcuts import render
from .models import program, minister, projects, BackgroundImageHomeSlider, Church_info, Work_process
from blog.models import Blog
from pages.forms import Subscribers
from pages.models import PICDesk
from django.contrib import messages
from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        form_subscibe = Subscribers(request.POST)
        if form_subscibe.is_valid():
            form_subscibe.save()
            
            messages.success(request, f'Your email address has been received successfully, we\'ll get back to you asap. Thanks !')
            return redirect('home')
    else:
        form_subscibe = Subscribers()
        
    context = {
        'title': 'RCCG Jesus THrone',
        'form_subscibe': form_subscibe,
        'our_work_process': Work_process.objects.all(),
        'pic_desk': PICDesk.objects.all(),
        'backgroundslider': BackgroundImageHomeSlider.objects.all(),
        'minister': minister.objects.all(),
        'church_infos': Church_info.objects.all(),
        'project': projects.objects.all(),
        'program': program.objects.all(),
        'blogs': Blog.objects.all(),
    }
    return render(request, 'home/home.html', context)