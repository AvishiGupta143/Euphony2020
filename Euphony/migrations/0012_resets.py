# Generated by Django 3.0.5 on 2020-06-10 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Euphony', '0011_eventform_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Key', models.CharField(blank=True, max_length=1000000)),
                ('Generator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Euphony.Profile')),
            ],
        ),
    ]
