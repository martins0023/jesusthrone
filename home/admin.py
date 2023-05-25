from django.contrib import admin
from .models import program, minister, projects, BackgroundImageHomeSlider, Church_info, Work_process

admin.site.register(program)
admin.site.register(Church_info)
admin.site.register(minister)
admin.site.register(projects)
admin.site.register(BackgroundImageHomeSlider)
admin.site.register(Work_process)