from django.db import models
from django.utils import timezone
from django.urls import reverse
#from django.core.urlresolvers import reverse

#here we are simply defining our database
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING,)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    #any method inside class should have self
    def publish(self):
        self.published_date =timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail")

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('myfirstblog.Post',related_name='comments',on_delete=models.DO_NOTHING,)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
