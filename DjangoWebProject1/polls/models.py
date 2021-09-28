from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    #string methods are convinient; they allow you to see the question text when viewing the questions list

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #custom method to check if the question was published in the last one day


class Choice(models.Model):

    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


"""
Following relationships “backward”
If a model has a ForeignKey, instances of the foreign-key model will 
have access to a Manager that returns all instances of the first model. 
By default, this Manager is named FOO_set, where FOO is the source model name, 
lowercased. This Manager returns QuerySets, which can be filtered and 
manipulated as described in the “Retrieving objects” section above.

This allows us to access choice_set from the Question model
"""