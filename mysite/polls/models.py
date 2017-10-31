from django.db import models
import datetime
from django.utils import timezone


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now > self.pub_date > now - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'date published'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    mytest = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.choice_text
