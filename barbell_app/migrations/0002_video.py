# Generated by Django 2.2 on 2021-04-11 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbell_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=155)),
                ('video', models.FileField(upload_to='video/%y')),
            ],
        ),
    ]