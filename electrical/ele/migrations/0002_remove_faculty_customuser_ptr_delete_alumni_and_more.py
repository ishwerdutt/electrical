# Generated by Django 4.0.6 on 2023-03-13 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ele', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='customuser_ptr',
        ),
        migrations.DeleteModel(
            name='Alumni',
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
    ]