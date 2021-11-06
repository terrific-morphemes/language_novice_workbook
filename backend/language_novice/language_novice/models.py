from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)


class Language(models.Model):
    name = models.CharField(max_length=30)


class Unit(models.Model):
    name = models.CharField(max_length=30)
    level = models.IntegerField()


class Lesson(models.Model):
    name = models.CharField(max_length=30)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)


class Exercise(models.Model):
    prompt = models.TextField()
    sample_answer = models.TextField()
    answer = models.TextField()
    completed = models.BooleanField(default=False)
    resources = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
