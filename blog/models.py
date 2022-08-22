from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250)
    parent_post = models.ForeignKey('Post', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
