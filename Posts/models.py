from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    POST_TYPES = [
        (0, 'Text'),
        (1, 'Review'),
        (2, 'Poem'),
    ]

    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500, blank=True)
    type = models.IntegerField(choices=POST_TYPES)
    date_created = models.DateTimeField(blank=True, default=datetime.now)

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='users',
                               related_query_name='user',
                               )

    class Meta:
        ordering = ['date_created', '-title']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title + ' (' + self.author + ')'

    def __repr__(self):
        return self.title + ' / ' + self.author + ' / ' + self.type
