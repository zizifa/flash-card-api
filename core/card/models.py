from django.db import models

# Create your models here.

class FlashCard(models.Model):
    # author=
    question=models.TextField()
    answer=models.TextField()

    def __str__(self):
        return self.question

# class Author(models.Model):
#     name=models.CharField(max_length=50)
