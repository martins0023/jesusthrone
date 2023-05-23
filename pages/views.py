from django.shortcuts import render, redirect
from .models import aboutUs, ContactImage, Jthrone_acct, SundaySermonSubscriber, PICDesk
from home.models import projects, minister, BackgroundImageHomeSlider, Church_info
from django.contrib import messages
from .forms import make_request, Subscribers

def pastordesk(request):
    if request.method == 'POST':
        form_subscibe = Subscribers(request.POST)
        if form_subscibe.is_valid():
            form_subscibe.save()
            
            messages.success(request, f'Your email address has been received successfully, we\'ll get back to you asap. Thanks !')
            return redirect('about')
    else:
        form_subscibe = Subscribers()
        
    context = {
        'form_subscibe': form_subscibe,
        'title': 'Pastor\'s Desk',
        'the_title': 'Pastor\'s Desk',
        'pic_desk': PICDesk.objects.all(),
        'ministers': minister.objects.all(),
        'project': projects.objects.all(),
        'church_infos': Church_info.objects.all(),
        'side_image': ContactImage.objects.all(),
        'background': BackgroundImageHomeSlider.objects.all(),
        'account': Jthrone_acct.objects.all(),
    }
    return render(request, 'pages/pastordesk.html', context)

def about(request):
    if request.method == 'POST':
        form_subscibe = Subscribers(request.POST)
        if form_subscibe.is_valid():
            form_subscibe.save()
            
            messages.success(request, f'Your email address has been received successfully, we\'ll get back to you asap. Thanks !')
            return redirect('about')
    else:
        form_subscibe = Subscribers()
        
    context = {
        'form_subscibe': form_subscibe,
        'title': 'About Us',
        'the_title': 'About Us',
        'minister': minister.objects.all(),
        'aboutus': aboutUs.objects.all(),
        'church_infos': Church_info.objects.all(),
        'side_image': ContactImage.objects.all(),
        'background': BackgroundImageHomeSlider.objects.all(),
    }
    return render(request,  'pages/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = make_request(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Your information has been received successfully, we\'ll get back to you asap with the info provided. Thanks !')
            return redirect('contact')
    else:
        form = make_request()
        
    
    if request.method == 'POST':
        form_subscibe = Subscribers(request.POST)
        if form_subscibe.is_valid():
            form_subscibe.save()
            
            messages.success(request, f'Your email address has been received successfully, we\'ll get back to you asap. Thanks !')
            return redirect('contact')
    else:
        form_subscibe = Subscribers()
        
    context = {
        'form_subscibe': form_subscibe,
        'form': form,
        'title': 'Contact',
        'the_title': 'Contact Us',
        'aboutus': aboutUs.objects.all(),
        'church_infos': Church_info.objects.all(),
        'side_image': ContactImage.objects.all(),
        'background': BackgroundImageHomeSlider.objects.all(),
    }
    return render(request,  'pages/contact.html', context)

def project(request):
    if request.method == 'POST':
        form_subscibe = Subscribers(request.POST)
        if form_subscibe.is_valid():
            form_subscibe.save()
            
            messages.success(request, f'Your email address has been received successfully, we\'ll get back to you asap. Thanks !')
            return redirect('project')
    else:
        form_subscibe = Subscribers()
        
    context = {
        'form_subscibe': form_subscibe,
        'title': 'Project',
        'the_title': 'Our Projects',
        'ministers': minister.objects.all(),
        'project': projects.objects.all(),
        'church_infos': Church_info.objects.all(),
        'background': BackgroundImageHomeSlider.objects.all(),
    }
    return render(request,  'pages/projects.html', context)

def onlinegiving(request):
    if request.method == 'POST':
        form_subscibe = Subscribers(request.POST)
        if form_subscibe.is_valid():
            form_subscibe.save()
            
            messages.success(request, f'Your email address has been received successfully, we\'ll get back to you asap. Thanks !')
            return redirect('onlinegiving')
    else:
        form_subscibe = Subscribers()
        
    context = {
        'form_subscibe': form_subscibe,
        'title': 'Online Giving',
        'the_title': 'Tithes, Offering, Donations, Giving',
        'ministers': minister.objects.all(),
        'project': projects.objects.all(),
        'church_infos': Church_info.objects.all(),
        'background': BackgroundImageHomeSlider.objects.all(),
        'account': Jthrone_acct.objects.all(),
    }
    return render(request,  'pages/onlinegiving.html', context)