from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


class Photo(models.Model):
    # realted_name : 연결된 객체에서 하위 객체의 목록을 부를 때 사용할 이름
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username + " " +  self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-updated']





