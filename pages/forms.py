from django import forms
from django.contrib.auth.models import User
from .models import Message, SundaySermonSubscriber

class make_request(forms.ModelForm):
    full_name = forms.CharField()
    email_address = forms.EmailField(help_text='A valid email address is required.e.g myemail@email.com')
    subject = forms.CharField()
    message = forms.Textarea()
        
    class Meta:
        model = Message
        fields = ['full_name', 'email_address', 'subject', 'message']

class Subscribers(forms.ModelForm):
    email_address = forms.EmailField()
    
    class Meta:
        model = SundaySermonSubscriber
        fields = ['email_address']
        
        
