import email
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Blog(models.Model):
    category = {
        ('Digging Deep', 'Digging Deep'),
        ('Faith Clinic', 'Faith Clinic'),
        ('Sunday School', 'Sunday School'),
        ('Open Heavens', 'Open Heavens'),
        ('Holy Ghost Service', 'Holy Ghost Service'),
        ('Annaual Convention', 'Annaual Convention'),
        ('Hymns', 'Hymns'),
        ('House Fellowship', 'House Fellowship'),
        ('Sunday Sermon', 'Sunday Sermon'),
        ('Anniversary', 'Anniversary'),
        ('Talks', 'Talks'),
        ('Motivation', 'Motivation'),
        ('Article', 'Article'),
    }
    blog_title = models.CharField(max_length=300)
    date_posted = models.DateField(default=timezone.now)
    blog_description = models.TextField(max_length=40000)
    #content_paragraph_title = models.CharField(max_length=300, default=None)
    #content_paragraph_1 = models.TextField(max_length=4000, default=None)
    blog_image = models.ImageField(default='blog.jpg', upload_to='blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_category = models.CharField(max_length=300, choices=category, default=None)
    
    def __str__(self):
        return self.blog_title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.blog_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (400, 200)
            img.thumbnail(output_size)
            img.save(self.blog_image.path)
            
class Comment(models.Model):
    full_name = models.CharField(max_length=200, default="Your name")
    email_address = models.EmailField(max_length=200, default="Email address")
    message = models.TextField()
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)