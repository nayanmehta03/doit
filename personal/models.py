from django.db import models
from user.models import DoitUser


# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(DoitUser, on_delete=models.CASCADE)

    def __str__(self):
        return "NAME: " + self.name + "\nOWNER: " + str(self.owner)


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField()
    ongoing = models.BooleanField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return "NAME: " + self.name + "\nBOARD: " + str(self.board)
