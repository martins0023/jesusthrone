from django.db import models
from PIL import Image

class ContactImage(models.Model):
    image = models.ImageField(default=None, upload_to='contact_image')
    
    def __str__(self):
        return 'image'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (434, 821)
            img.thumbnail(output_size)
            img.save(self.image.path)

class aboutUs(models.Model):
    heading = models.CharField(max_length=500, default='Our Story In the Redeemed Christian Church of God')
    aboutIntro = models.CharField(max_length=7000, default='Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line')
    Ourhistory = models.TextField(help_text='please make this history in three paragraphs respectively', max_length=2000)
    OurhistoryP2 = models.TextField(max_length=40000)
    OurhistoryP3 = models.TextField(max_length=40000)
    ChurchImage = models.ImageField(default='church.jpg', upload_to='church_about')
    ChurchImage2 = models.ImageField(default='church.jpg', upload_to='church_about')
    ChurchImage3 = models.ImageField(default='church.jpg', upload_to='church_about')
    
    def __str__(self):
        return self.heading
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.ChurchImage.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 377)
            img.thumbnail(output_size)
            img.save(self.ChurchImage.path)
            
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.ChurchImage2.path)
        if img.height > 300 or img.width > 300:
            output_size = (800, 908)
            img.thumbnail(output_size)
            img.save(self.ChurchImage2.path)
            
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.ChurchImage3.path)
        if img.height > 300 or img.width > 300:
            output_size = (320, 424)
            img.thumbnail(output_size)
            img.save(self.ChurchImage3.path)
            
class Jthrone_acct(models.Model):
    account_type = {
        ('RCCG PROJECT ACCOUNT', 'RCCG PROJECT ACCOUNT DETAILS'),
        ('RCCG JESUS THRONE ZONAL ACCOUNT DETAILS', 'RCCG JESUS THRONE ZONAL ACCOUNT DETAILS'),
        ('RCCG JESUS THRONE YOUTH ACCOUNT DETAILS', 'RCCG JESUS THRONE YOUTH ACCOUNT DETAILS'),
        ('RCCG JESUS THRONE ACCOUNT DETAILS', 'RCCG JESUS THRONE ACCOUNT DETAILS'),
        ('OTHERS', 'OTHERS')
    }
    account_name = models.CharField(max_length=300, default='RCCG JESUS THRONE ACCOUNT DETAILS')
    account_type = models.CharField(max_length=300, default='OTHERS', choices=account_type)
    account_number = models.CharField(max_length=300, default='2123587356')
    account_bank = models.CharField(max_length=300, default='UBA BANK')
    
    def __str__(self):
        return self.account_name
    
class Message(models.Model):
    full_name = models.CharField(max_length=200, default="Your name")
    email_address = models.EmailField(max_length=200, default="Email address")
    subject = models.CharField(max_length=300, default="Subject")
    message = models.TextField()
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
class SundaySermonSubscriber(models.Model):
    email_address = models.EmailField(max_length=300, default="Email address")
    
    def __str__(self):
        return self.email_address
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
class PICDesk(models.Model):
    content_title = models.CharField(max_length=1000)
    content = models.TextField(max_length=30000)
    content_image = models.ImageField(default='PIC.jpg', upload_to='PIC_DESK')
    PIC_name = models.CharField(max_length=1000, default='')
    
    def __str__(self):
        return self.content_title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)