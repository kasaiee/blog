from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS_COICES = (
    ('DF', 'Draft'),
    ('PB', 'Published')
)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='PB')

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=2, default='DF', choices=STATUS_COICES)
    author = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        null=True
    )
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self):
        return self.title