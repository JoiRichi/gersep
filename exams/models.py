
# Create your models here.
'''
!) Create an exam page. in this page, there will be a running time, candidate code on top, textfield and submit button
2)

'''
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class QuestionForCandidate(models.Model):
    question_text = models.CharField(max_length=1000)
    start_time= models.DateTimeField(null=True, blank=True,)
    deadline= models.DateTimeField(null=True, blank=True,)

    def __str__(self):
        return self.question_text



class Submission(models.Model):
    question=models.ForeignKey(QuestionForCandidate, on_delete=models.CASCADE, null=True, blank=True)
    email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=get_user_model())
    #student_email=  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=False, default= get_user_model())
    candidate_code = models.CharField(max_length=200, default= 'GER/EDO/AN/INT/00')
    text = models.TextField(max_length=2000 )

    submit_date = models.DateTimeField(default= timezone.now())
    score = models.FloatField(default=0)



    def __str__(self):
        return self.candidate_code

