from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class QuestionModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    question_text = models.CharField(max_length=250)
    
    choice = (
        ('pub', 'published'),
        ('dra', 'draft')
    )
    status = models.CharField(max_length=3, choices=choice)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Question'

    def __str__(self):
        return self.question_text


class AnswerModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer')
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name='answer')

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Answer'

    def __str__(self):
        return self.choice_text
