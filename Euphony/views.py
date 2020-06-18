import smtplib
import ssl
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Images, Branch, Events, Domain, Team, Gallery, Profile, EventForm, Resets, DeletedAccounts
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
import random
import time
from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static


def Homepage(request):
    Data = {
        'EuphonyLogo': Images.objects.get(Name='EuphonyLogo').File.url,
        'BG1': Images.objects.get(Name='BG1').File.url,
        'BG': Images.objects.get(Name='BG2').File.url,
        # 'BG10': Images.objects.get(Name='BG10').File.url,
        # 'BGEDITOR': Images.objects.get(Name='BGEDITOR').File.url,
        # 'BG15': Images.objects.get(Name='BG15').File.url,
        # 'BG16': Images.objects.get(Name='BG16').File.url,
        'BG17': Images.objects.get(Name='BG17').File.url,
        # 'BG18': Images.objects.get(Name='BG18').File.url,
        # 'BG19': Images.objects.get(Name='BG19').File.url,
        # 'BG14': Images.objects.get(Name='BG14').File.url,
        'Vocalist': Images.objects.get(Name='Vocalist').File.url,
        'Guitarist': Images.objects.get(Name='Guitarist').File.url,
        'Percussion': Images.objects.get(Name='Percussion').File.url,
        'Pianist': Images.objects.get(Name='Pianist').File.url,
        'Drum': Images.objects.get(Name='Drum').File.url,
        'DJmix': Images.objects.get(Name='DJmix').File.url,
        'MIXMASTER': Images.objects.get(Name='MIXMASTER').File.url,
        'Upcoming': Images.objects.get(Name='Upcoming').File.url,
        'Ongoing': Images.objects.get(Name='Ongoing').File.url,
        'Jam': Images.objects.get(Name='Jam').File.url,
        'Convocation': Images.objects.get(Name='Convocation').File.url,
        'Freshers': Images.objects.get(Name='Freshers').File.url,
        'Garba': Images.objects.get(Name='Garba').File.url,
        'Gandhi': Images.objects.get(Name='Gandhi').File.url,
        'Bandish': Images.objects.get(Name='Bandish').File.url,
        'Farewell': Images.objects.get(Name='Farewell').File.url,
        'AKTU': Images.objects.get(Name='AKTU').File.url,
        'Pallab': Images.objects.get(Name='Pallab').File.url,
        'IIT18': Images.objects.get(Name='IIT18').File.url,
        'MNNIT': Images.objects.get(Name='MNNIT').File.url,
        'ZONALS18': Images.objects.get(Name='ZONALS18').File.url,
        'ABES19': Images.objects.get(Name='ABES19').File.url,
        'ZEALCON19': Images.objects.get(Name='ZEALCON19').File.url,
        'ZONALS19': Images.objects.get(Name='ZONALS19').File.url,
        'ROPAR20': Images.objects.get(Name='ROPAR20').File.url,
        'ABES20': Images.objects.get(Name='ABES20').File.url,
        'ZONALS20': Images.objects.get(Name='ZONALS20').File.url,
        'ZONALSBOB20': Images.objects.get(Name='ZONALSBOB20').File.url,
        'ARPIT': Images.objects.get(Name='ARPIT').File.url,
        # 'ARPITT': Images.objects.get(Name='ARPITT').File.url,
        'SAUBHAGYA': Images.objects.get(Name='SAUBHAGYA').File.url,
        'ISHITA': Images.objects.get(Name='ISHITA').File.url,
        # 'ISHITAA': Images.objects.get(Name='ISHITAA').File.url,
        # 'Editor': Images.objects.get(Name='Editor').File.url,
        'EDITOR': Images.objects.get(Name='EDITOR').File.url,
        'AKGECLOGO': Images.objects.get(Name='AKGECLOGO').File.url,
    }
    if request.user.id is not None:
        Data.update({'Profile': Profile.objects.get(Email=request.user.email)})
    return render(request, 'Homepage.html', Data)


def EventsPage(request):
    Data = {
        'EuphonyLogo': Images.objects.get(Name='EuphonyLogo').File.url,
        'BG19': Images.objects.get(Name='BG19').File.url,
        'Events': Events.objects.all(),
    }
    if request.user.id is not None:
        Data.update({'Profile': Profile.objects.get(Email=request.user.email)})
    return render(request, 'Events.html', Data)


def TeamPage(request):
    Data = {
        'BG16': Images.objects.get(Name='BG16').File.url,
        'ARPIT': Images.objects.get(Name='ARPIT').File.url,
        'FourthYearTeamMembers': Team.objects.filter(Year='4').order_by('Year'),
        'ThirdYearTeamMembers': Team.objects.filter(Year='3').order_by('Year'),
        'SecondYearTeamMembers': Team.objects.filter(Year='2').order_by('Year'),
    }
    return render(request, 'Team.html', Data)


def GalleryPage(request):
    Data = {
        'Pro1': Images.objects.get(Name='Pro1').File.url,
        'Events': Events.objects.all(),
        'Jam': Images.objects.get(Name='Jam').File.url,
        'Convocation': Images.objects.get(Name='Convocation').File.url,
        'Freshers': Images.objects.get(Name='Freshers').File.url,
        'Garba': Images.objects.get(Name='Garba').File.url,
        'Gandhi': Images.objects.get(Name='Gandhi').File.url,
        'Bandish': Images.objects.get(Name='Bandish').File.url,
        'Farewell': Images.objects.get(Name='Farewell').File.url,
        'AKTU': Images.objects.get(Name='AKTU').File.url,
        'REVERBGALLERY': Images.objects.get(Name='REVERBGALLERY').File.url,
        'Random': Images.objects.get(Name='Random').File.url,
        'Landcrafts': Images.objects.get(Name='Landcrafts').File.url,
        'Saksham': Images.objects.get(Name='Saksham').File.url,
        'ROPAR20': Images.objects.get(Name='ROPAR20').File.url,
        'JammingSession': Images.objects.get(Name='JammingSession').File.url,
    }
    return render(request, 'Gallery.html', Data)


def ParticularAlbum(request, Album):
    Data = {
        'Pro1': Images.objects.get(Name='Pro1').File.url,
        'Albums': Gallery.objects.filter(EventName=f'{Album}').order_by('EventName'),
        'Name': Album,
    }
    return render(request, 'ParticularAlbum.html', Data)


def Help(request):
    if request.method == 'POST':
        sender = "euphonyakgechelp@gmail.com"
        password = "euphony@123"
        port = 465
        recieve1 = 'avishigupta143@gmail.com'
        cont = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=cont) as server:
            server.login(sender, password)
            subject = 'Euphony Query'
            body = f"""Query From = {request.POST['Student_Name']}
                    The Email ID = {request.POST['Student_Email']}
                    The Query is = {request.POST['message']}
                                """
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(sender, recieve1, message)
        return redirect('/Euphony')
    Data = {
        'BG18': Images.objects.get(Name='BG18').File.url,
    }
    if request.user.id is not None:
        Data.update({'Profile': Profile.objects.get(Email=request.user.email)})
    return render(request, 'Help.html', Data)


def Register(request):
    if request.user.id is not None:
        return redirect('/Euphony/Homepage')
    if request.method == 'POST':
        if request.POST['Password1'] != request.POST['Password2']:
            messages.info(request, 'Password Should Match')
            return redirect('/Euphony/Register')
        elif User.objects.filter(email=request.POST['Student_Email']).exists():
            messages.info(request, 'Email In Use')
            return redirect('/Euphony/Register')
        else:
            print(request.POST)
            print(request.FILES)
            NewUser = User()
            NewUser.username = f'EU_{random.randint(20, 909090)}' + request.POST['Student_Name'].split()[0][:1]
            NewUser.first_name = request.POST['Student_Name'].split()[0]
            NewUser.last_name = request.POST['Student_Name'].split()[1]
            NewUser.email = request.POST['Student_Email']
            NewUser.set_password(request.POST['Password1'])
            NewUser.save()
            New = Profile()
            New.user = NewUser
            New.Student_Name = request.POST['Student_Name']
            New.DOB = request.POST['Student_DOB']
            New.Branch = Branch.objects.get(Branch_Name=request.POST['Student_Branch'].upper())
            New.Email = request.POST['Student_Email']
            New.Year = request.POST['Student_Year']
            New.Address = request.POST['Student_Address']
            New.Contact = request.POST['Student_Contact']
            New.Student_ProfilePic = request.FILES['Image']
            New.save()
            return redirect('/Euphony/Login')
    else:
        Data = {
            'BG10': Images.objects.get(Name='BG10').File.url,
            'MIC': Images.objects.get(Name='MIC').File.url,
        }
        if request.user.id is not None:
            Data.update({'Profile': Profile.objects.get(Email=request.user.email)})
        return render(request, 'Register.html', Data)


def Login(request):
    if request.method == 'POST':
        email = request.POST['Student_Email']
        password = request.POST['Password1']
        if User.objects.filter(email=email).exists():
            usercurrentpassword = User.objects.get(email=email).password
            if check_password(password, usercurrentpassword):
                USER = auth.authenticate(username=User.objects.get(email=email).username, password=password)
                auth.login(request, USER)
                return redirect('/Euphony')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('/Euphony/Login')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/Euphony/Login')
    else:
        # GET PART
        Data = {
            'EuphonyLogo': Images.objects.get(Name='EuphonyLogo').File.url,
            'BG17': Images.objects.get(Name='BG17').File.url,
        }
        if request.user.id is not None:
            Data.update({'Profile': Profile.objects.get(Email=request.user.email)})
        return render(request, 'Login.html', Data)


def Logout(request):
    auth.logout(request)
    return redirect('/Euphony')


def YourProfile(request):
    Data = {
        'BG10': Images.objects.get(Name='BG10').File.url,
        'Pro2': Images.objects.get(Name='Pro2').File.url,
        'EDITOR': Images.objects.get(Name='EDITOR').File.url,
    }
    if request.user.id is not None:
        Data.update({'Profile': Profile.objects.get(Email=request.user.email)})
    return render(request, 'Your Profile.html', Data)


def EditProfile(request):
    if request.method == 'POST':
        New = Profile.objects.get(Email=request.user.email)
        New.Student_Name = request.POST['Student_Name']
        New.Email = request.POST['Email']
        New.Contact = request.POST['Contact']
        New.Address = request.POST['Address']
        New.Year = request.POST['Year']
        if 'DP' in request.FILES:
            New.Student_ProfilePic = request.FILES['DP']
        New.save()
        return redirect('/Euphony/YourProfile')
    Data = {
        'BG10': Images.objects.get(Name='BG10').File.url,
        'Pro2': Images.objects.get(Name='Pro2').File.url,
        'EDITOR': Images.objects.get(Name='EDITOR').File.url,
    }
    if request.user.id is not None:
        Data.update({'Profile': Profile.objects.get(Email=request.user.email)})
    return render(request, 'EditProfile.html', Data)


def EventsForm(request, Name):
    if request.method == 'POST':
        print(request.POST)
        New = EventForm()
        New.Student = Profile.objects.get(Email=request.user.email)
        New.Event = Events.objects.get(Name=request.POST['EventName'])
        New.Domain = Domain.objects.get(Name=request.POST['Domain'])
        if 'AudiVideo' in request.FILES:
            New.Audition_Video = request.FILES['AudiVideo']
        if 'AudiLink' in request.POST:
            New.Audition_Link = request.POST['AudiLink']
        New.save()
        sender = "euphonyakgechelp@gmail.com"
        password = "euphony@123"
        port = 465
        recieve1 = f"{request.POST['Student_Email']}"
        cont = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=cont) as server:
            server.login(sender, password)
            subject = 'Successfully Registered Confirmation'
            body = f""" You've been successfully registered for the Event : {request.POST['EventName']}
                        You will reached out soon!
                        Thankyou,
                        Regards,
                        Team Euphony
                    """
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(sender, recieve1, message)
        time.sleep(2)
        return redirect('/Euphony/Events')
    else:
        # GET PART
        Data = {
            'BG11': Images.objects.get(Name='BG11').File.url,
            'Registering_For': Events.objects.get(Name=Name),
            'Domains': Domain.objects.all(),
        }
        if request.user.id is not None:
            Data.update({'Profile': Profile.objects.get(Email=request.user.email)})
        return render(request, 'EventForm.html', Data)


def Settings(request):
    if request.method == 'POST':
        n = random.randint(150000, 999999)
        if Resets.objects.filter(Generator=Profile.objects.get(user=User.objects.get(email=request.user.email))).exists():
            Resets.objects.get(Generator=Profile.objects.get(user=User.objects.get(email=request.user.email))).delete()
        New = Resets()
        New.Generator = Profile.objects.get(user=User.objects.get(email=request.user.email))
        New.Key = n
        New.save()
        sender = "euphonyakgechelp@gmail.com"
        password = "euphony@123"
        port = 465
        recieve1 = f"{request.user.email}"
        cont = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=cont) as server:
            server.login(sender, password)
            subject = 'Email Verification Code'
            body = f""" Verification Code for your request is: {n}
                                            Thankyou,
                                            Regards,
                                            Team Euphony
                                        """
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(sender, recieve1, message)
        return redirect('/Euphony/Verification')
    Data = {
        'BG10': Images.objects.get(Name='BG10').File.url,
        'USER': Profile.objects.get(user__email=request.user.email),
        'Change': 'none',
        'Delete': 'none',
        'Verify': 'none',
        'Button1': '620px',
        'Button2': '620px',
        'Button3': '620px',
    }
    return render(request, 'Settings.html', Data)


def Verification(request):
    if request.method == 'POST':
        a = Resets.objects.get(Generator=Profile.objects.get(user=User.objects.get(email=request.user.email)))
        if a.Key == request.POST['Code']:
            N = Profile.objects.get(user=User.objects.get(email=request.user.email))
            N.Verified = 'True'
            N.save()
            return redirect('/Euphony')
        else:
            messages.info(request, 'Invalid Code')
            return redirect('/Euphony/Verification')
    else:
        # GET PART
        Data = {
            'BG10': Images.objects.get(Name='BG10').File.url,
        }
        return render(request, 'VerificationCode.html', Data)


def ForgotPassword(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['Email']).exists():
            if Resets.objects.filter(Generator=Profile.objects.get(user=User.objects.get(email=request.POST['Email']))).exists():
                Resets.objects.get(Generator=Profile.objects.get(user=User.objects.get(email=request.POST['Email']))).delete()
            n = random.randint(150000, 999999)
            New = Resets()
            New.Generator = Profile.objects.get(user=User.objects.get(email=request.POST['Email']))
            New.Key = n
            New.save()
            sender = "euphonyakgechelp@gmail.com"
            password = "euphony@123"
            port = 465
            recieve1 = f"{request.POST['Email']}"
            cont = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=cont) as server:
                server.login(sender, password)
                subject = 'Password Reset Code'
                body = f""" Verification Code for your request is: {n}
                                    Thankyou,
                                    Regards,
                                    Team Euphony
                                """
                message = f'Subject: {subject}\n\n{body}'
                server.sendmail(sender, recieve1, message)
            messages.info(request, f"{request.POST['Email']}")
            return redirect('/Euphony/PasswordVerification')
        else:
            messages.info(request, 'Invalid Email ID Please Enter Valid Email ID.')
            return redirect('/Euphony/ForgotPassword')
    Data = {
        'BG10': Images.objects.get(Name='BG10').File.url,
    }
    return render(request, 'ForgotPasword.html', Data)


def PasswordVerification(request):
    if request.method == 'POST':
        U = User.objects.get(email=request.POST['Email'])
        P = Profile.objects.get(Email=U.email)
        ToCheck = Resets.objects.get(Generator=P)
        if ToCheck.Key == request.POST['Code']:
            messages.info(request, f"{request.POST['Email']}")
            return redirect('/Euphony/ForgotPasswordChange')
        else:
            messages.info(request, f"{request.POST['Email']}")
            messages.info(request, 'Invalid Code')
            return redirect('/Euphony/PasswordVerification')
    else:
        Data = {
            'BG10': Images.objects.get(Name='BG10').File.url,
        }
        return render(request, 'PasswordVerification.html', Data)


def ForgotPasswordChange(request):
    if request.method == 'POST':
        New = User.objects.get(email=request.POST['EMAIL'])
        New.set_password(request.POST['Password'])
        New.save()
        time.sleep(3)
        return redirect('/Euphony/Login')
    Data = {
        'BG10': Images.objects.get(Name='BG10').File.url,
    }
    return render(request, 'ForgotPasswordChange.html', Data)


def ChangeMyPassword(request):
    if request.method == 'POST':
        USER = User.objects.get(email=request.user.email)
        current = USER.password
        entered = request.POST['CURR']
        newenter = request.POST['NEW']
        if check_password(entered, current):
            New = User.objects.get(email=request.user.email)
            New.set_password(newenter)
            New.save()
            update_session_auth_hash(request, New)
            time.sleep(3)
            return redirect('/Euphony/Settings')
        else:
            messages.info(request, 'Incorrect Current Password')
            Data = {
                'BG10': Images.objects.get(Name='BG10').File.url,
                'USER': Profile.objects.get(user__email=request.user.email),
                'Change': 'inherit',
                'Delete': 'none',
                'Verify': 'none',
                'Button1': '100px',
                'Button2': '100px',
                'Button3': '100px',
            }
            return render(request, 'Settings.html', Data)


def DeleteAccount(request):
    if request.method == 'POST':
        USER = User.objects.get(email=request.user.email)
        to_delete = request.user.email
        current = USER.password
        entered = request.POST['Password']
        if check_password(entered, current):
            New = DeletedAccounts()
            New.Name = Profile.objects.get(user=request.user).Student_Name
            New.Contact = Profile.objects.get(user=request.user).Contact
            New.Reason = request.POST['Reasons']
            New.Explanation = request.POST['message']
            New.Email = request.user.email
            New.save()
            auth.logout(request)
            DEL = User.objects.get(email=to_delete)
            DEL.delete()
            return redirect('/Euphony')
        else:
            messages.info(request, 'Incorrect Current')
            Data = {
                'BG10': Images.objects.get(Name='BG10').File.url,
                'USER': Profile.objects.get(user__email=request.user.email),
                'Change': 'none',
                'Delete': 'inherit',
                'Verify': 'none',
                'Button1': '100px',
                'Button2': '100px',
                'Button3': '100px',
            }
            return render(request, 'Settings.html', Data)

