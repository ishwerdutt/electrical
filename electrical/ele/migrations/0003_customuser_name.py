# Generated by Django 4.0.6 on 2023-03-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ele', '0002_remove_faculty_customuser_ptr_delete_alumni_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
