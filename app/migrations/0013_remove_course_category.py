# Generated by Django 5.0.4 on 2024-04-30 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_course_course_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
    ]
