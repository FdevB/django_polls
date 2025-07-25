from django.db import models

from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class QuestionModel(models.Model):
    """
    Model definition for QuestionModel.

    This class defines the QuestionModel database schema and its related behaviors.

    Attributes:
        author (ForeignKey to User): Author of the post.
        question_text (CharField): Question text of the question.
        STATUS_CHOICES (variable): All choices for status.
        status (CharField): Choose status of the post (published or draft) from STATUS_CHOICES.
        created_at (DateField): Date when the post was created.
        updated_at (DateField): Date when the post was last updated.
        published_at (DateTimeField): Date and time when the post was published.
        slug (SlugField): Slug derived from the title (non-editable).
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    question_text = models.CharField(max_length=250)
    
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('dra', 'Draft')
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='dra')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Question'

    def __str__(self):
        return self.question_text
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save method to automatically set the slug field.
        """ 

        self.slug = slugify(self.question_text)


        if (self.status == 'pub') and (self.published_at is None):
            self.published_at = timezone.now()

        elif (self.published_at is not None) and (timezone.now() >= self.published_at):
            self.status = 'pub'

        else:
            self.status = 'dra'

        super().save(*args, **kwargs)


class AnswerModel(models.Model):
    """
    Model definition for AnswerModel.

    This class defines the AnswerModel database schema and its related behaviors.

    Attributes:
        author (ForeignKey to User): Author of the post.
        question (ForeignKey to QuestionModel): Answer to this question.
        choice_text (CharField): Answer text.
        votes (IntegerField): Count of votes.
        send_at (DateTimeField): Date when the post was sent.
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer')
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name='answer')

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    send_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Answer'

    def __str__(self):
        return self.choice_text
