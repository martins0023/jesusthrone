from email.policy import default
from django.db import models
from PIL import Image

class BackgroundImageHomeSlider(models.Model):
    background_slider_title = models.CharField(max_length=300)
    background_slider_info = models.TextField(max_length=500)
    image_slider = models.ImageField(default=None, upload_to='backgroundslider')
    
    def __str__(self):
        return self.background_slider_title
        

class minister(models.Model):
    minister_name = models.CharField(max_length=300)
    minister_title = models.CharField(max_length=300)
    minister_info = models.TextField(max_length=500)
    minister_pic = models.ImageField(default='minister.jpg', upload_to='minister')
    
    def __str__(self):
        return self.minister_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.minister_pic.path)
        if img.height > 300 or img.width > 300:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.minister_pic.path)

class projects(models.Model):
    project_choices = {
        ('Provincial', 'Provincial'),
        ('Zone', 'Zone'),
        ('Regional', 'Regional'),
        ('Others', 'Others'),
    }
    project_title = models.CharField(max_length=300)
    project_description = models.TextField(max_length=500)
    project_image = models.ImageField(default='project.jpg', upload_to='project')
    project_type = models.CharField(max_length=255, choices=project_choices, default='Zone')
    
    def __str__(self):
        return self.project_title
    
    #def save(self, *args, **kwargs):
    #    super().save(*args, **kwargs)
        
    #    img = Image.open(self.project_image.path)
    #    if img.height > 300 or img.width > 300:
    #        output_size = (400, 400)
    #        img.thumbnail(output_size)
    #        img.save(self.project_image.path)

class program(models.Model):
    program_title = models.CharField(max_length=200)
    program_info = models.TextField(max_length=500)
    program_image = models.ImageField(default='program.jpg', upload_to='programs')
    
    def __str__(self):
        return self.program_title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.program_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.program_image.path)

class Church_info(models.Model):
    church_name = models.CharField(max_length=100)
    church_mail = models.CharField(max_length=100)
    church_mobile = models.CharField(max_length=100)
    church_address = models.CharField(max_length=500)
    
    church_youtube_account = models.URLField(max_length=500, default="https://www.youtube.com")
    church_facebook_account = models.URLField(max_length=500, default="https://www.facebook.com")
    church_twitter_account = models.URLField(max_length=500, default="https://www.twitter.com")
    church_tiktok_account = models.URLField(max_length=500, default="https://www.tiktok.com")
    church_instagram_account = models.URLField(max_length=500, default="https://www.instagram.com")
    
    year_founded = models.CharField(max_length=300, help_text='add year founded', default='2008')
    no_of_house_fellowship_centers = models.IntegerField(default=6)
    no_of_parishes_created = models.IntegerField(default=10)
    
    
    image = models.ImageField(default='default.jpg', upload_to='org_info_image')
    
    def __str__(self):
        return self.church_name
    
class Work_process(models.Model):
    work_process_icon_choices = {
        ('hand-shake', 'hand-shake'),
        ('answer', 'answer'),
        ('sketch', 'sketch'),
        ('house-1', 'house-1'),
    }
    process_id = models.IntegerField()
    work_process_title = models.CharField(max_length=255)
    work_process_content = models.TextField(max_length=2000)
    work_process_icon = models.CharField(max_length=255, choices=work_process_icon_choices, default='hand-shake')
    
    def __str__(self):
        return self.work_process_title