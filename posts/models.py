from django.db import models
from users.models import BlogUser
from category.models import Category
from tags.models import Tag
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.unique_slug_field import unique_slug_generator

class Post(models.Model):

    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    tag = models.ManyToManyField(Tag)

    slug = models.SlugField(max_length=50, null=True, blank=True)

    image = models.ImageField(null=True, blank=True)

    show_in_sample = models.BooleanField(default=False)

    featured = models.BooleanField(default=False)

    class Meta:

        ordering = ("-created",)

    def __str__(self):

        return self.title

class Gallery(models.Model):

    image = models.ImageField(upload_to="gallery/")

    class Meta:

        verbose_name = "Gallery"
        
        verbose_name_plural = ("Galleries")

@receiver(post_save,sender=Post)
def blog_post_save_reciver(sender, instance, created, **kwargs):
    post_save.disconnect(blog_post_save_reciver, sender=Post)
    print(created)
    if not instance.slug:
        # print("If")
        instance.slug = unique_slug_generator(instance) 
        instance.save()
    post_save.connect(blog_post_save_reciver, sender=Post)