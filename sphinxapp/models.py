from django.db import models
import djangosphinx

class Student(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    address=models.TextField()

    def __str__(self):
        return self.name

class Question(models.Model):
    question=models.SlugField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer=models.SlugField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer