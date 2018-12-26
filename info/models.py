from django.db import models
from django.utils import timezone


class MatchInformation(models.Model):
    match_website = models.CharField(max_length=200)
    match_start_date = models.DateTimeField('match start time')
    match_before_start = models.CharField(max_length=200)
    match_name = models.CharField(max_length=200)
    match_writer = models.CharField(max_length=200)
    match_register = models.CharField(max_length=200)
    match_time_length = models.CharField(max_length=200)

    def __str__(self):
        return self.match_name

    def was_expired(self):
        return not self.match_start_date >= timezone.now()


class Test(models.Model):
    test_name = models.CharField('test', max_length=200)

    def __str__(self):
        return self.test_name

