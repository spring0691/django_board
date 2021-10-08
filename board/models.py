from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from acc.models import User

# Create your models here.
class Board(models.Model):
    subject = CharField(max_length=100)
    writer = CharField(max_length=30)
    content = TextField()
    likey = IntegerField(default=0)
    up = models.ManyToManyField(User)
    c_time = models.DateTimeField()

    def _str_(self):
        return self.subject

class Reply(models.Model):
    subject = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=100)
    comment = models.TextField()
    pic = models.ImageField()