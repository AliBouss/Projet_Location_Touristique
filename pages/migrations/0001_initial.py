# Generated by Django 3.2.6 on 2021-08-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=123)),
                ('last_name', models.CharField(max_length=123)),
                ('designation', models.TextField()),
                ('photo', models.ImageField(upload_to='photo/%Y:%m/%d/')),
                ('facebook_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
