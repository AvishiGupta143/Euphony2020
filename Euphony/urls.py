from django.urls import path
from django.conf.urls import url
from Euphony import views
from django.conf import settings
from django.conf.urls.static import static


# app_name = 'Euphony'

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('Homepage', views.Homepage, name='Homepage'),
    path('Events', views.EventsPage, name='Events'),
    path('Team', views.TeamPage, name='Team'),
    path('Gallery', views.GalleryPage, name='Gallery'),
    path('Album/<str:Album>', views.ParticularAlbum, name='ParticularAlbum'),
    path('Help', views.Help, name='Help'),
    path('Register', views.Register, name='Register'),
    path('Login', views.Login, name='Login'),
    path('Logout', views.Logout, name='Logout'),
    path('YourProfile', views.YourProfile, name='Your Profile'),
    path('EventForm/<str:Name>', views.EventsForm, name='EventForm'),
    path('EditProfile', views.EditProfile, name='EditProfile'),
    path('Settings', views.Settings, name='Settings'),
    path('Verification', views.Verification, name='Verification'),
    path('ForgotPassword', views.ForgotPassword, name='ForgotPassword'),
    path('PasswordVerification', views.PasswordVerification, name='PasswordVerification'),
    path('ForgotPasswordChange', views.ForgotPasswordChange, name='ForgotPasswordChange'),
    path('ChangeMyPassword', views.ChangeMyPassword, name='ChangeMyPassword'),
    path('DeleteAccount', views.DeleteAccount, name='DeleteAccount'),
]
