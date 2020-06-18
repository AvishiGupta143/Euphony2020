from django import template
from django.shortcuts import render, redirect
import requests
from Euphony.models import Images, Branch, Events, Domain, Profile, EventForm
from django.contrib.auth.models import User, auth

register = template.Library()


@register.filter(name='CheckIfRegistered')
def CheckIfRegistered(CURRUSER, EVENTNAME):
    S = User.objects.get(username=CURRUSER)
    if EventForm.objects.filter(Student__Student_Name=Profile.objects.get(Email=S.email).Student_Name, Event__Name=EVENTNAME).exists():
        return True
    else:
        return False


@register.filter(name='CheckFileType')
def CheckFileType(NAME):
    print(NAME)
    if NAME.endswith('.mp4'):
        return 'video'
    elif NAME.endswith('.MOV'):
        return 'video'
    else:
        return 'img'