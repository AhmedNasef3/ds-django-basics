from django.contrib import admin
from .models import Post,Author
#from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    #summernote_fields = '__all__'
    list_display=['title','author']
    list_filter=['tags','author']
    search_fields=['title','content']

# my own class 
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','email']
    search_fields=['name','email']

admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)