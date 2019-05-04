from django.contrib import admin
from .models import Post, Gallery, Comment

class PostAdmin(admin.ModelAdmin):

    list_display = ('id','user', 'title', 'category', 'created', 'updated_at',"show_in_sample",'featured')

    list_editable = ( 'title','category',"show_in_sample",'featured')

    list_filter = ('created',)

    search_fields = ('user', 'title', 'created', 'updated_at', )

    list_display_links = ('user',)

    list_per_page = 15

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Gallery)