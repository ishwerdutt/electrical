# Generated by Django 4.0.6 on 2023-04-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ele', '0008_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='company',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='subjects',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
