# Generated by Django 3.2.6 on 2021-08-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=123),
        ),
    ]