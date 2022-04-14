from django.db import models

# Create your models here.
class Vote(models.Model):
    subject = models.CharField(max_length=150)
    choice_one = models.CharField(max_length=300)
    choice_two = models.CharField(max_length=300)
    vote_one = models.IntegerField(default=0)
    vote_two = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    vote = models.ForeignKey(
        Vote,
        on_delete= models.CASCADE,
    )
    choice = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    