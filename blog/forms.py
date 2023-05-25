from django import forms
from django.contrib.auth.models import User
from .models import Comment

class Make_request(forms.ModelForm):
    full_name = forms.CharField()
    email_address = forms.EmailField(help_text='A valid email address is required.e.g myemail@email.com')
    message = forms.Textarea()
        
    class Meta:
        model = Comment
        fields = ['full_name', 'email_address', 'message']