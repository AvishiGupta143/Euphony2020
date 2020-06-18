# Generated by Django 3.0.5 on 2020-06-02 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Euphony', '0003_auto_20200603_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Audition_Video', models.FileField(blank=True, upload_to='')),
                ('Audition_Link', models.URLField(blank=True)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Euphony.Domain')),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Euphony.Events')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(blank=True, max_length=100)),
                ('Student_ProfilePic', models.FileField(upload_to='')),
                ('DOB', models.DateField()),
                ('Email', models.EmailField(max_length=100)),
                ('Year', models.CharField(blank=True, max_length=5)),
                ('Address', models.CharField(blank=True, default='', max_length=100)),
                ('Contact', models.CharField(blank=True, default='+91-', max_length=14)),
                ('Branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Euphony.Branch')),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.AddField(
            model_name='eventform',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Euphony.Profile'),
        ),
    ]