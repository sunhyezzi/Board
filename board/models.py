from django.db import models
# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50]


class Comment(models.Model):
    board= models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    
    def __str__(self):
        return (self.author.username if self.author else "무명") + "의 댓글" 