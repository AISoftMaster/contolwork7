from django.db import models

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=50, blank=False)
    dateTime = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.question


class Choice(models.Model):
    answer = models.CharField(max_length=100, blank=False)
    asking = models.ForeignKey('poll.Poll', related_name='ask_poll', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class Answer(models.Model):
    poll = models.ForeignKey('poll.Poll', related_name='answer_poll', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    choice = models.ForeignKey('poll.Choice', related_name='answer_choice', on_delete=models.CASCADE)
