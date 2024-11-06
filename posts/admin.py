from django.contrib import admin

# Register your models here.
from .models import post,Author
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(admin.ModelAdmin):
    #list_display=['title','author']
    list_filter=['author','tags']
    search_fields=['title','content']
    #summernote_fields = ('content',)

admin.site.register(post,PostAdmin)
admin.site.register(Author)