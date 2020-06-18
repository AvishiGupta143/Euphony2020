from django.db import models
from django.contrib.auth.models import User, auth


class Images(models.Model):
    Name = models.CharField(max_length=100, blank=True)
    File = models.FileField()

    def __str__(self):
        return self.Name


class Domain(models.Model):
    Name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.Name


class Events(models.Model):
    Name = models.CharField(max_length=100, blank=True)
    Date = models.DateField()
    Poster = models.FileField()
    Description = models.CharField(max_length=100000, default="", blank=True)
    Rules = models.FileField()

    def __str__(self):
        return self.Name


class Branch(models.Model):
    Branch_Name = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.Branch_Name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Student_Name = models.CharField(max_length=100, blank=True)
    Student_ProfilePic = models.FileField()
    DOB = models.DateField()
    Email = models.EmailField(max_length=100)
    Year = models.CharField(max_length=5, blank=True)
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    RollNo = models.CharField(max_length=12, default='1702713031', blank=True)
    Address = models.CharField(max_length=100, default="", blank=True)
    Contact = models.CharField(default='+91-', blank=True, max_length=14)
    Verified = models.CharField(max_length=10, default='False', blank=True)

    def __str__(self):
        return self.Student_Name


class EventForm(models.Model):
    Student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Event = models.ForeignKey(Events, on_delete=models.CASCADE)
    Domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    Audition_Video = models.FileField(blank=True)
    Audition_Link = models.URLField(blank=True)

    def __str__(self):
        return self.Student.Student_Name + ' registered for ' + self.Event.Name


class Team(models.Model):
    Name = models.CharField(max_length=50, blank=True)
    Year = models.CharField(max_length=2, default='')
    Domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)
    Picture = models.FileField(blank=True)
    FB_Link = models.CharField(max_length=10000000, blank=True)
    Insta_Link = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.Name


class Gallery(models.Model):
    EventName = models.CharField(max_length=100, blank=True, default='')
    Picture = models.FileField(blank=True, default='')

    def __str__(self):
        return self.EventName


class Resets(models.Model):
    Generator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Key = models.CharField(max_length=1000000, blank=True)

    def __str__(self):
        return self.Generator.Student_Name + ' reset code is ' + self.Key


class DeletedAccounts(models.Model):
    Name = models.CharField(max_length=100, blank=True)
    Email = models.CharField(max_length=100, blank=True)
    Contact = models.CharField(max_length=100, blank=True)
    Reason = models.CharField(max_length=10000, blank=True)
    Explanation = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.Name + " deleted his/her Account."