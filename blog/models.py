from django.db import models

from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    photo = models.ImageField(default='logo.png', upload_to='posts')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class PageDescription(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='blog_pagehome')
    title_text = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    photo = models.ImageField(default='logo.png', upload_to='pageImg')

    def __str__(self):
        return self.title

# class PageHome(PageDescription):
#    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_pagehome')


class Gallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_gallery')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
#    photo = models.ImageField(default='logo.png', upload_to='gallery')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class PhotoForGallery(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    # ForeignKey auto. generates OneToMany relationship
    # to access all Photos in a Gallery use Gallery.objects.all()[0].photoforgallery_set.all()
    photo = models.ImageField(default='logo.png', upload_to='gallery')
