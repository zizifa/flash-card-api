from django.db import models
from django.contrib.auth import authenticate


class FlashCard(models.Model):

    question=models.TextField()
    answer=models.TextField()

    def __str__(self):
        return self.question

