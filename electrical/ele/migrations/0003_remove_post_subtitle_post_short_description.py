# Generated by Django 4.0.6 on 2023-04-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ele', '0002_alter_post_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.CharField(blank=True, default='no short description available', max_length=100),
        ),
    ]
