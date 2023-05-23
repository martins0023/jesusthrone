from django.contrib import admin
from .models import aboutUs, ContactImage, Jthrone_acct, Message, SundaySermonSubscriber, PICDesk

admin.site.register(Message)
admin.site.register(aboutUs)
admin.site.register(ContactImage)
admin.site.register(Jthrone_acct)
admin.site.register(SundaySermonSubscriber)
admin.site.register(PICDesk)