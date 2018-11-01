from django.test import TestCase
from django.contrib.auth import get_user_model
from groups.models import Group
# Create your tests here.
from django.urls import reverse
from django.utils.text import slugify






User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts')
    created_at = models.DateTimeField(auto_now = True)
    message = models.TextField()
    message_html = models.TextField(editable=False,default='',blank = True)
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True)


    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = slugify(message)
        super().self.save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={})


    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']
