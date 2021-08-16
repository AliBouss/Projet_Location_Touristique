from django.db import models


class Team(models.Model):
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    designation = models.CharField(max_length=123)
    facebook_link = models.URLField(max_length=123, blank=True)
    linkedin_link = models.CharField(max_length=123, blank=True)
    twitter_link = models.URLField(max_length=123, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    photo = models.ImageField(upload_to="photos", blank=True)

    def __str__(self):
        return self.first_name
