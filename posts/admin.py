from django.contrib import admin
from .models import Post, Gallery, Comment

class PostAdmin(admin.ModelAdmin):

    list_display = ('id','author', 'title', 'category', 'created', 'updated_at',"show_in_sample",'featured')

    list_editable = ( 'title','category',"show_in_sample",'featured')

    list_filter = ('created',)

    search_fields = ('author', 'title', 'created', 'updated_at', )

    list_display_links = ('author',)

    list_per_page = 15

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Gallery)